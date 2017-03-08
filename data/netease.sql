create table songs (
  id  INTEGER AUTO_INCREMENT,
  sid char(16),
  name text,
  singer text,
  neteaseUrl text,
  mp3Url text,
  flag char(16) default 'default' -- default, processed, dead
);
