export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  // Getter para code
  get code() {
    return this._code;
  }

  // Setter para code
  set code(value) {
    this._code = value;
  }

  // Getter para name
  get name() {
    return this._name;
  }

  // Setter para name
  set name(value) {
    this._name = value;
  }

  // Método para mostrar la moneda en el formato especificado
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
