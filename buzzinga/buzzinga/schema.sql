drop table if exists users;
create table users (
	id integer primary key autoincrement,
	email text not null,
	username text not null,
	phone text not null, 
	password text not null
);

drop table if exists posts;
create table posts (
	pid integer primary key autoincrement,
	title text not null,
	description text not null
);

drop table if exists posted_by;
create table posted_by (
	post_id integer not null,
        u_id integer not null,
	FOREIGN KEY(post_id) REFERENCES posts(pid)
	FOREIGN KEY(u_id) REFERENCES users(id)	
);

