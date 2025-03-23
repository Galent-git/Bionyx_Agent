import faker

class FunFactModule:
    name = "FunFactModule"
    description = "Share a random fun fact."

    def __init__(self):
        self.faker = Faker()

    def handle(self):
        # Generate a fun fact using Faker
        fact = self.faker.sentence(nb_words=10)
        print("Bionyx [Fun Fact]:", fact)
