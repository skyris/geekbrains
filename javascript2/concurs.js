function isPalindrome(s){
  s=s.replace(/\W/g,'').toUpperCase();
  return s==s.split('').reverse().join('')
}
