export default function guardrail(mathFunction) {
  const queue = [];

  try {
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    queue.push(error.message || error.toString()); // Ensure we get only the message or a string
  } finally {
    queue.push('Guardrail was processed');
  }

  return queue;
}
