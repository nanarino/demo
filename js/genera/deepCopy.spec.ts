import deepCopy from './deepCopy';

const KEY = Symbol('☘')

console.log(deepCopy({
    [KEY]: 1,
    name: 'test'
}));

