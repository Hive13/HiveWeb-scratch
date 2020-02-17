# Members

Endpoint: `/api/admin/members`

endpoints: 
- [ ] /members
	- [ ] /
        - current index route redirects to profile
        - should we do something else with index or do the same?
	- [ ] /edit
	- [ ] /info
	- [ ] /password
	- [x] /profile
    	- input:
        	- `member_id`
      	- output:
        	- whole member row(?)
        	- ^ that's what it does now (20200217)
	- [ ] /search