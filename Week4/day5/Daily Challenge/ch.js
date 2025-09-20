function isAnagram(str1, str2) {
  const normalize = (str) =>
    str.replace(/\s+/g, '').toLowerCase().split('').sort().join('');

  return normalize(str1) === normalize(str2);
}