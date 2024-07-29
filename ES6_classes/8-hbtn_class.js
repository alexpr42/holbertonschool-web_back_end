export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  set size(newSize) {
    this._size = newSize;
  }

  get location() {
    return this._location;
  }

  set location(newLocation) {
    this._location = newLocation;
  }

  valueOf() {
    // This method is called when the object is cast to a Number
    return this._size;
  }

  toString() {
    // This method is called when the object is cast to a String
    return this._location;
  }
}
