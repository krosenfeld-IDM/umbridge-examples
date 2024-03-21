import emcee
from umbridge.emcee import UmbridgeLogProb
import arviz as az
import argparse
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":

    # Read URL and nwalkers from command line arguments
    parser = argparse.ArgumentParser(description='emcee sampler for 2D rosenbrock example')
    parser.add_argument('--url', metavar='url', type=str, default='http://localhost:4243',
                        help='The ULR on which the model is running, for example http://localhost:4243')
    parser.add_argument('--nwalkers', type=int, default=32,
                        help='the number of walkers for the MCMC sampler (default: 32)')
    args = parser.parse_args()
    print(f'Connecting to host URL {args.url}')

    # Create an instance of UmbridgeLogProb with the specified URL and target name
    log_prob = UmbridgeLogProb(args.url, 'posterior')

    nwalkers = args.nwalkers
    # Create an instance of EnsembleSampler with the specified number of walkers, dimensions, and log probability function
    sampler = emcee.EnsembleSampler(nwalkers, log_prob.ndim, log_prob)

    # Run the MCMC sampler for 100 steps starting from random positions selected from a Gaussian distribution centered at (0, 0)
    p0 = np.random.randn(nwalkers, log_prob.ndim)
    state = sampler.run_mcmc(p0, 100)

    # Convert the sampler output to an InferenceData object
    inference_data = az.from_emcee(sampler)

    # Plot pairwise scatter plots of the inferred parameters
    az.plot_pair(inference_data)

    # Adjust the layout and save the plot as 'emcee_inference.png'
    plt.tight_layout()
    plt.savefig('emcee_inference.png')

    print(az.summary(inference_data, round_to=2))