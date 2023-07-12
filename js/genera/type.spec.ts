import type from './type';

console.log(type(1));
console.log(type(true));
console.log(type('string'));
console.log(type(undefined));
console.log(type(null));
console.log(type({}));
console.log(type([]));
console.log(type(new Set()));
console.log(type(new Map()));
console.log(type(new Date()));
console.log(type(/(.*)/));
console.log(type(() => { }));
console.log(type(async function* () { }));
