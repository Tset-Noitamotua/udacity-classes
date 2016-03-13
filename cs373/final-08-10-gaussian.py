def gaussian_product(mu, sigma2, nu, r2):
    mu_prime = (r2 * mu + sigma2 * nu) * 1. / (sigma2 + r2)
    sigma2_prime = 1. / ( 1. / sigma2 + 1. / r2)
    return mu_prime, sigma2_prime

print gaussian_product(1., 1., 1., 1.)
print gaussian_product(1., 1., 5., 1.)
print gaussian_product(1., 1., 5., 4.)

