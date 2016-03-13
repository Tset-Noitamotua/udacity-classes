def gaussian_additive(mu, sigma2, u, r2):
    mu_prime = mu + u
    sigma2_prime = sigma2 + r2
    return mu_prime, sigma2_prime

print gaussian_additive(1., 1., 1., 1.)
print gaussian_additive(1., 1., 5., 1.)
print gaussian_additive(1., 1., 5., 4.)

