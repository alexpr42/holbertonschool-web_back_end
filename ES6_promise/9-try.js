export default function guardrail(mathFunction) {
  const queue = [];

  try {
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    queue.push(error.message); // Use error.message to get just the error message
  } finally {
    queue.push('Guardrail was processed');
  }

  return queue;
}
