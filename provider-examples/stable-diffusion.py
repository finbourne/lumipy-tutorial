import lumipy.provider as lp

lp.ProviderManager(
    lp.StableDiffusion(),
    port=5005
).run()
