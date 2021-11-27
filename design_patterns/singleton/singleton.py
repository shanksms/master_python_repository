from design_patterns.singleton.tigger import Tigger

t1 = Tigger()
t2 = Tigger()
assert id(t1) == id(t2)