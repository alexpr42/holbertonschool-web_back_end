// 8-clean_set.js
function cleanSet(set, startString = '') {
  if (typeof startString !== 'string') {
    throw new TypeError('startString must be a string');
  }

  return [...set]
    .filter((value) => typeof value === 'string' && value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');
}

export default cleanSet;
