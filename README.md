# Chat.Bpgc

We started this project just to learn about websockets and rest API's in web apps. We aim at creating a chat service for our campus. Some of the features we are working on include:

- [ ] Anonymous group chat using usernames
- [ ] Support both verified (via email) and non-verified users
- [ ] Anonymous one-to-one chat
- [ ] Additional facilities for verified users

This project is in active development and as such, not at all ready for usage. There could be bugs, issues and un-addressed features. We are working on them and any sort of help is appreciated. Above all, we are simply learning!

Currently we don't have a single startup script. So to run the project you need to start Django and Vue seperately. Here are the steps:

### Django

- `bash runserver.sh`

### Vue

- `cd chat-frontend`
- `npm install`
- `npm run serve`