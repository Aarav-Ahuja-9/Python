spice_mix = set() # set is also a data type which represents a collection of things
print(f"Initial ID of spice_mix {id(spice_mix)}")
print(f"Spice mix contains: {spice_mix}")
spice_mix.add("cumin")
spice_mix.add("coriander")
print(f"ID of spice_mix after adding cumin and coriander {id(spice_mix)}")
print(f"Spice mix contains: {spice_mix}")