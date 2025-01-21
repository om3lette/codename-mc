## User scenarios

### Telegram client

1. User changes their mc nickname 
2. User views their current mc nickname
3. User requests the service to create a new token - if token already exists, old token is returned
4. User or Admin deletes token
4. Admin adds user tg_id
5. Admin lists whole object plane (tg_id, mc_nickname, token)

### Minecraft client

1. Minecraft plugin sends authentication request with body like (mc_nickname, token)