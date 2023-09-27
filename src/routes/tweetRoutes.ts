import { Router } from 'express'
const router = Router();
// const {
//     authenticateUser,
//     authorizePermissions,
//   } = require('../middleware/authentication'); //ok

const { tweets,
    singleTweet,
    updateTweet,
    createTweet,
    deleteTweet} = require('../controllers/tweetRoutes')



router.route('/:id').get(singleTweet)
router.route('/').get(tweets)
router.route('/').post(createTweet)
router.route('/:id').patch(updateTweet)
router.route('/:id').delete(deleteTweet)


export default router