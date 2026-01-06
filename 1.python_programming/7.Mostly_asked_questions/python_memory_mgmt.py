'''
Question:
“How does Python manage memory? (Garbage collection basics)”

📌 Core Conceptual Answer (what to say in an interview)
👉 Python handles memory automatically using:
1️⃣ Reference Counting — keeps track of how many references point to each object.
2️⃣ Garbage Collector (GC) — handles cyclic references (e.g., objects that refer to each other, forming loops) which reference counting alone can’t clean up.

✅ This means you don’t need to manually free memory like in C/C++ — Python does it for you!

🧩 How it works
🔑 1️⃣ Reference Counting
Every object has an internal counter (refcount).

When a new reference is made → counter increases.

When a reference goes away → counter decreases.

When counter reaches zero → memory is reclaimed immediately.

✅ Example:

python
Copy
Edit
a = []  # refcount = 1
b = a   # refcount = 2
del a   # refcount = 1
del b   # refcount = 0 → memory freed
🔑 2️⃣ Garbage Collector
Reference counting fails for circular references:

python
Copy
Edit
class Node:
    def __init__(self):
        self.next = self

node = Node()
del node  # This alone won't free memory because `self.next` keeps a reference!
Python’s GC module detects such unreachable cycles.

It’s part of the gc module and runs periodically.

🗂️ How to control GC
✅ You can interact with it:

python
Copy
Edit
import gc

gc.collect()       # Force a garbage collection
gc.disable()       # Disable GC temporarily
gc.enable()        # Re-enable GC
✅ Usually, you don’t need to manage this — but it’s useful for performance tuning or debugging memory leaks.

📌 Memory Management Best Practices
✅ Python helps, but you should still:

Avoid huge unnecessary data structures.

Break circular references if possible.

Use weak references (weakref module) for caches to avoid cycles.

Use context managers (with open(...) as f:) to auto-close resources.

✅ Summary to say in an interview:
“Python uses a combination of reference counting and a cyclic garbage collector to manage memory automatically. Reference counting reclaims most objects immediately when their count drops to zero, and the garbage collector periodically removes unreachable objects with circular references. This makes Python memory-safe without needing manual deallocation.”

 In QA Automation:
Clean up large test data, API responses, or logs properly.
Close files, DB connections, and drivers (driver.quit()) to avoid leaks.
For big frameworks, monitor memory usage to catch slow leaks.
'''