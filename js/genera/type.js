function type(obj){
    let str = ({}).toString.call(obj)
    return str.slice(8,str.length-1).toLowerCase()
}