import { Router } from 'express'
const router = Router();
// const {
//     authenticateUser,
//     authorizePermissions,
//   } = require('../middleware/authentication');

const {singleUser, users, createUser, updateUser,deleteUser} = require('../controllers/user')



router.route('/:id').get(singleUser)
router.route('/').get(users)
router.route('/').post(createUser)
router.route('/:id').patch(updateUser)
router.route('/:id').delete(deleteUser)


export default router