class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of this owner's pets by filtering the Pet.all list."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a pet to this owner after checking its type.
        Also, set the pet's owner to self."""
        if not isinstance(pet, Pet):
            raise Exception("Not a pet!")
        pet.owner = self
        return pet

    def get_sorted_pets(self):
        """Return the owner's pets sorted by pet name."""
        return sorted(self.pets(), key=lambda pet: pet.name)
