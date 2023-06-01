# Execy

The ececy exec_time decorator is a utility that measures the execution time of a function. It can be used to easily track and log the time taken by a function to execute, both for synchronous and asynchronous functions.

## Table of Contents

- [Execy](#execy)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)

## Installation

```bash
pip install execy
```

## Usage

To use the exec_time decorator, follow these steps:
```python
from execy import exec_time
import asyncio
import time

@exec_time
def sync_function():
    # Simulate a time-consuming synchronous task
    time.sleep(2)

@exec_time
async def async_function():
    # Simulate a time-consuming asynchronous task
    await asyncio.sleep(2)

# Call the decorated synchronous function
sync_function()

# Call the decorated asynchronous function
asyncio.run(async_function())
```

The result will be

```bash
Function 'sync_function' executed in 2.0001089572906494 seconds.
Function 'async_function' executed in 2.001432180404663 seconds.

```
