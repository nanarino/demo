//base64toUint8Array
const base64toUint8Array = base64 => {
    const raw = window.atob(base64);
    const arr = new Uint8Array(new ArrayBuffer(raw.length));
    return arr.map((v, i) => raw.charCodeAt(i))
}

//uint8ArrayToBase64
const uint8ArrayToBase64 = uint8Array => window.btoa([].map.call(uint8Array, v => String.fromCharCode(v)).join(''));


//Array contained pixel point color data
//像素点类数组类
class Pxpoint extends Array {
    constructor(...args) {
        super(...args)
    }
    //web安全色
    toWebSafeColor() {
        return this.map(
            (v, i) => {
                if (i >= 3) return v
                if (v < 26) return 0
                if (v < 77) return 51
                if (v < 179) return 153
                if (v < 230) return 204
                return 255
            }
        )
    }
    //create Pxpoint(RGBA[...all 0-255]) from HSLA[H:360*n deg, S:0-100%, L:0-100%, alpha:0-255]
    //静态方法，将HSL数组转化为RGBA数组形式的像素点对象
    static from(hslaArray) {
        hslaArray[0] %= 360
        const [h, s, l, a] = hslaArray.map((v, i) => (v / [360, 100, 100, 255][i]))
        let r, g, b
        if (s == 0) {
            r = g = b = l;//achromatic
        } else {
            const hue2rgb = (p, q, t) => {
                if (t < 0) t += 1;
                if (t > 1) t -= 1;
                if (t < 1 / 6) return p + (q - p) * 6 * t;
                if (t < 1 / 2) return q;
                if (t < 2 / 3) return p + (q - p) * (2 / 3 - t) * 6;
                return p;
            }
            let q = l < 0.5 ? l * (1 + s) : l + s - l * s;
            let p = 2 * l - q;
            r = hue2rgb(p, q, h + 1 / 3);
            g = hue2rgb(p, q, h);
            b = hue2rgb(p, q, h - 1 / 3);
        }
        return new Pxpoint(...([r, g, b, a].map(v => Math.round(255 * v))))
    }
}




//Canvas Pixel Serialized Tools Class
//像素序列化器类
class PxSerializer extends Array {
    constructor(uint8ClampedArray, width, height) {
        //get Uint8ClampedArray data and reshape
        //将Uint8ClampedArray（或其他4*h*w的类数组如Uint8Array）以矩阵（三维数组）呈现
        super(...Array.from(uint8ClampedArray)
            .reduce((a, v, point) => (point % 4 ? a[a.length - 1].push(v) : a.push(new Pxpoint([v])), a), [])
            .reduce((a, v, row) => (row % width ? a[a.length - 1].push(v) : a.push([v]), a), [])
        )
        Object.defineProperty(this, "width", {
            value: width,
            writable: true,
            enumerable: false,
        });
        Object.defineProperty(this, "height", {
            value: height,
            writable: true,
            enumerable: false,
        });
    }
    //flatten and ceateImageData
    //将像素序列化对象转换为ImageData对象，
    //经常使用.call(矩阵,宽,高)使其他符合矩阵格式（三维数组）转换
    toImageData(width = this.width, height = this.height) {
        return new ImageData(Uint8ClampedArray.from(this.toString().split(',').map(v => +v)), width, height)
    }
    //将像素序列化对象转换为无压缩的base64
    toRawBase64() {
        return uint8ArrayToBase64(Uint8ClampedArray.from(this.toString().split(',').map(v => +v)))
    }
    //以无压缩的base64构造像素序列化对象
    static fromRawBase64(base64, width, height) {
        return new PxSerializer(base64toUint8Array(base64), width, height)
    }
}




//PxPainter
//像素画工具类
class PxPainter {
    constructor(context, width, height, limitWidth = 0, limitHeight = 0) {
        this.org = context;
        Object.defineProperty(this, "width", {
            value: width || context.canvas.getAttribute('width'),
            writable: true,
            enumerable: false,
        });
        Object.defineProperty(this, "height", {
            value: height || context.canvas.getAttribute('height'),
            writable: true,
            enumerable: false,
        });
        this.data = new PxSerializer(context.getImageData(
            limitWidth,
            limitHeight,
            limitWidth + this.width,
            limitHeight + this.height).data, this.width, this.height);
    }
    //putImageData
    //将ImageData对象渲染到画布，默认渲染的是对象本身的data
    save(imageData, limitWidth = 0, limitHeight = 0) {
        if (!imageData) {
            imageData = this.data.toImageData()
            this.org.putImageData(imageData, limitWidth, limitHeight)
        } else {
            this.org.putImageData(imageData, limitWidth, limitHeight)
            //如果渲染的是外来的ImageData对象（一般是data.toImageData.call的或者PxSerializer.fromRawBase64构造的）,渲染后将重新获取一次data
            this.data = new PxSerializer(this.org.getImageData(
                limitWidth,
                limitHeight,
                limitWidth + this.width,
                limitHeight + this.height).data, this.width, this.height);
        }
    }
    //转base64 参数默认是'image/png'
    toDataURL(...args) {
        return this.org.canvas.toDataURL(args)
    }
    saveToWebSafeColors() {
        this.data = this.data.map(row => row.map(p => Pxpoint.prototype.toWebSafeColor.call(p)))
        this.data.width = this.width
        this.save()
    }
    //从base64转img异步渲染 渲染后将重新获取一次data
    fromDataURL(src, limitWidth = 0, limitHeight = 0) {
        const image = new Image()
        image.src = src
        image.onload = () => {
            this.org.drawImage(image, limitWidth, limitHeight);
            this.data = new PxSerializer(this.org.getImageData(
                limitWidth,
                limitHeight,
                limitWidth + this.width,
                limitHeight + this.height).data, this.width, this.height);
        }
    }
}