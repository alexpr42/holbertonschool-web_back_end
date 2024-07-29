export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;

    // Validación en el constructor
    if (typeof this._name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    if (typeof this._length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    if (!Array.isArray(this._students) || !this._students.every(student => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
  }

  // Getter para name
  get name() {
    return this._name;
  }

  // Setter para name
  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  // Getter para length
  get length() {
    return this._length;
  }

  // Setter para length
  set length(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = value;
  }

  // Getter para students
  get students() {
    return this._students;
  }

  // Setter para students
  set students(value) {
    if (!Array.isArray(value) || !value.every(student => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = value;
  }
}
