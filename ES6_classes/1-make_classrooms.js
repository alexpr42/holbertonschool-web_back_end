import ClassRoom from './0-classroom'; // Eliminar la extensión .js

export default function initializeRooms() {
  return [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34),
  ];
}
