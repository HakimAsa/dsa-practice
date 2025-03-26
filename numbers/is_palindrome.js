// solution for an integer to be palindromic in javascript
function is_palindrome(num) {
  if (num < 0 || (num % 10 === 0 && num !== 0)) return false
  num = num.toString()
  let left = 0
  let right = num.length - 1
  while (left < right) {
    if (num[left] !== num[right]) return false
    left++
    right--
  }
  return true
}
//test cases

console.log(is_palindrome(12321)) // true
console.log(is_palindrome(121)) // true
console.log(is_palindrome(12345)) // false
console.log(is_palindrome(123210)) // false
console.log(is_palindrome(10)) // false
console.log(is_palindrome(123456)) // false
console.log(is_palindrome(-121)) // false
console.log(is_palindrome(0)) // true
