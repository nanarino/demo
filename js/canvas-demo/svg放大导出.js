/**
 * 将svg导出成图片
 * @param svg DOM节点 => document.querySelectorAll('svg')[?]
 * @param name 生成的图片文件名
 * @param magnification 生成的图片宽高的放大倍数 （svg是矢量图放大不糊）
 * @param type 生成的图片后缀默认png
 */
export const svgSave = (svg, name, magnification = 1, type = 'png') => {
    let serializer = new XMLSerializer()
    let source = '<?xml version="1.0" standalone="no"?>\r\n' + serializer.serializeToString(svg)
    let image = new Image()
    image.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(source)
    document.body.appendChild(image)
    image.onload = function () {
        let canvas = document.createElement('canvas')
        canvas.width = image.clientWidth * magnification
        canvas.height = image.clientHeight * magnification
        let context = canvas.getContext('2d')
        context.drawImage(image, 0, 0, canvas.width, canvas.height)
        let a = document.createElement('a')
        a.download = `${name}.${type}`
        a.href = canvas.toDataURL(`image/${type}`)
        a.click()
    }
}