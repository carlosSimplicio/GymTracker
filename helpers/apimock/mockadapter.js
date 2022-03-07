export function mockapi(data) {
    return new Promise((resolve, reject) => {
        setTimeout(()=>resolve({data: data ? JSON.parse(JSON.stringify(data)) : null}), 1000)
    })
}

export function mockapierror(error) {
    return new Promise((resolve, reject) => {
        setTimeout(()=>reject(new Error(error)), 1000)
    })
}