export default function (obj: any) {
    const tag = ({}).toString.call(obj)
    return tag.slice(8, tag.length - 1).toLowerCase()
}