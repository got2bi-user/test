import rx
from rx import operators
source = rx.of("Alpha","Delta","Gamma")
disp = source.subscribe(lambda x: print(f"Received {x}"), lambda ex: print(ex), print("complited"))
