import React, { useState, useEffect } from 'react'

function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  },[])

  return (
    <div>

        {(typeof data.dogs === 'undefined') ? (
          <p>Loading...</p>
        ) : (
          data.dogs.map(dog, i) => (
              <p key={i}>{dogs}</p>
          ))
        )}
      
    </div>
  )
}

export default App