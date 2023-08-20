import { Request, Response } from 'express';


const users =async (req: Request, res: Response) => {
    res.send('users')
}

const singleUser = async(req: Request, res: Response)=>{
    res.send('no user now')
}

const createUser = async(req: Request, res: Response)=>{
    res.send('user created')
}

const updateUser = async (req: Request, res: Response)=>{
    res.send('update created')
}

const deleteUser = async (req: Request, res: Response)=>{
    res.send('delete created')
}

// export default {
//     singleUser,
//     users,
//     createUser,
//     updateUser,
//     deleteUser
// };

module.exports = {
    singleUser,
    users,
    createUser,
    updateUser,
    deleteUser
}