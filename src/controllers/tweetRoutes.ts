import { Request, Response } from 'express';
import { PrismaClient } from '@prisma/client';



const tweets =async (req: Request, res: Response) => {
    res.send('users')
}

const singleTweet = async(req: Request, res: Response)=>{
    res.send('no user now')
}

const createTweet = async(req: Request, res: Response)=>{
    res.send('user created')
}
// dfdfdf
const updateTweet = async (req: Request, res: Response)=>{
    res.send('update created')
}

//B MEIN  N

const deleteTweet = async (req: Request, res: Response)=>{
    res.send('delete created')
}


// gigigig

// export default {
//     singleUser,
//     users,
//     createUser,
//     updateUser,
//     deleteUser
// };

module.exports = {
    tweets,
    singleTweet,
    updateTweet,
    createTweet,
    deleteTweet
}