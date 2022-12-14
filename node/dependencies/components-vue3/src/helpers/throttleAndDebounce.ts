export function throttleAndDebounce(fn: () => void, delay: number): () => void {
  let timeout: ReturnType<typeof setTimeout>
  let called = false

  return () => {
    if (timeout) {
      clearTimeout(timeout)
    }

    if (!called) {
      fn()
      called = true
      setTimeout(() => {
        called = false
      }, delay)
    } else {
      timeout = setTimeout(fn, delay)
    }
  }
}