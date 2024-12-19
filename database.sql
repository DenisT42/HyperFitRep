create database if not exists hyperfit_DB;

use hyperfit_DB;

create table users
(
    id int auto_increment primary key,
    username varchar(50) unique not null ,
    email varchar(100) unique not null ,
    password varchar(25) not null ,
    create_at timestamp
);

create table workout_plans (
    id int primary key auto_increment,
    user_id int not null ,
    name varchar(100) not null ,
    description text ,
    created_at timestamp,
    foreign key (user_id) references users (id)
);


create table exercises (
    id int primary key auto_increment,
    name varchar(100) not null ,
    instructions text ,
    image_url varchar(255) ,
    difficulty int
);


create table workout_exercises (
    id int primary key auto_increment ,
    workout_plan_id int not null ,
    exercises_id int not null ,
    duration int ,
    calories_burned int ,
    heart_rate int ,
    foreign key (workout_plan_id) references workout_plans (id),
    foreign key (exercises_id) references exercises (id)
);


create table progress_logs (
    id int primary key auto_increment,
    user_id int not null ,
    date date,
    workout_plan_id int,
    total_calories int,
    total_duration int,
    avg_heart_rate int,
    foreign key (user_id) references users (id),
    foreign key (workout_plan_id) references workout_plans (id)
);