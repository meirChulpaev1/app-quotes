interface Qoute{
    qoute:string,
    author:string,
    categories:string

}
function ShowQoute(prop:Qoute) {

    return (
        <>
        <br/>
            <div className='quote'>

            <h1>the qoute reandom:<br/>{prop.qoute}</h1>
            <br/>
            <h2>the author :<br/>{prop.author}</h2>
            <br/>
            <h2>categories:<br/>{prop.categories}</h2>
           
            </div>
        </>
    )
}

export default ShowQoute

