import React, { useState, useEffect } from 'react'
import axios from 'axios';
const App = props => {
    // useEffect(() => {
    //   axios.get('/api/test')
    //     .then(res => setState(res.data))
    // }, [])
const [state, setState] = useState('')
return(
    <div>
      <p>SR APP</p>
    </div>
 )
};
export default App;