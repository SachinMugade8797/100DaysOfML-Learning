
### Python Memory Management

1.  **Core Mechanisms**
    *   Python's memory management relies on a combination of **automatic garbage collection**, **reference counting**, and various internal optimisations.
    *   Understanding these helps in writing **efficient and robust applications**.

2.  **Reference Counting**
    *   **Primary Method**: This is the main way Python manages memory.
    *   **Concept**: Each object in Python keeps a **count of references** pointing to it.
    *   **Deallocation**: When this reference count drops to **zero**, the memory occupied by that object is automatically deallocated.
    *   **Example**: Using `sys.getrefcount()` shows that a variable and the `getrefcount` function call itself contribute to the count. Deleting a variable (e.g., `del B`) reduces its reference count, leading to deallocation if it reaches zero.

3.  **Garbage Collection (GC)**
    *   **Purpose**: Includes a **cyclic garbage collector** to specifically handle **reference cycles**.
    *   **Reference Cycles**: These occur when objects reference each other, causing their individual reference counts to never reach zero, which would otherwise result in memory leaks.
    *   **`gc` Module Functions**:
        *   **Enable/Disable**: `gc.enable()` to turn on automatic GC; `gc.disable()` to turn it off.
        *   **Manual Trigger**: `gc.collect()` forces a garbage collection run and returns the number of unreachable objects. This is particularly useful for breaking reference cycles.
        *   **Statistics**: `gc.get_stats()` provides per-generation statistics in a list of dictionaries, including collections, collected, and uncollectible items.
        *   **Unreachable Objects**: `gc.get_unreachable()` lists objects that are unreachable but could not be garbage collected (often due to cycles).

4.  **Memory Management Best Practices**
    *   **Use Local Variables**: They have a **shorter lifespan** and are freed sooner compared to global variables, leading to better memory usage.
    *   **Avoid Circular References**: These are a significant cause of **memory leaks** (e.g., `A = B`, `B = A`). Manual `gc.collect()` might be needed to free such objects.
    *   **Use Generators**: They improve memory efficiency by **producing items one at a time** using the `yield` keyword, keeping only one item in memory at any given moment.
    *   **Explicitly Delete Objects**: Use the **`del` statement** for variables and objects when they are no longer needed to free up memory.
    *   **Profile Memory Usage**: Employ tools like **`tracemalloc`** or `memory_profiler` to identify memory leaks and optimise usage. `tracemalloc` can track memory allocation, take snapshots, and provide statistics by line number to pinpoint memory-intensive parts of the code.
