import express from 'express'
const app = express()
import userRoutes from './routes/user'
import tweetRoutes from './routes/tweetRoutes'

app.use(express.json())

app.get('/', (req,res)=>{
    
    
    res.send("Twitter Backend Updated Again")
})



app.use('/user', userRoutes)
app.use('/tweet', tweetRoutes)

app.post('/user',(req,res)=>{
    res.status(501).json({error: 'Not Implemented'})
})







app.listen(3000, ()=>{
    console.log('Server is running on port 3000')
})