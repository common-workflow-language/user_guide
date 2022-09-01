/**
 * Capitalize each word passed. Will split the text by spaces.
 * @param {String} message - The input message.
 * @return {String} the message with each word with its initial letter capitalized.
 */
function capitalizeWords (message) {
  if (message === undefined || message === null || typeof message !== 'string' || message.trim().length === 0) {
    return '';
  }
  return message
    .split(' ')
    .map(function (token) {
      return token.charAt(0).toUpperCase() + token.slice(1);
    })
    .join(' ');
}
