create bot_habibs;
use bot_habibs;

create table Usuarios(
	ID_Usuario char(18),
	primary key (ID_Usuario)
);

create table Guilds(
	ID_Guild char(18),
    primary key(ID_Guild)
);

create table Aliases_Usuario(
	ID_Usuario char(18),
	ID_Guild char(18),
    Alias_Usuario varchar(75),
    primary key(ID_Usuario, ID_Guild, Alias_Usuario),
    foreign key (ID_Usuario) references Usuarios(ID_Usuario),
    foreign key (ID_Guild) references Guilds(ID_Guild)
);

create table Aliases_Guilds(
	ID_Guild char(18),
    Alias_Guild varchar(75),
    primary key(ID_Guild, Alias_Guild),
    foreign key (ID_Guild) references Guilds(ID_Guild)
);

create table Voice_Channels(
    ID_VC char(18),
    ID_Guild char(18),
    Vc_Name varchar(75),
    primary key(ID_VC, ID_Guild),
    foreign key(ID_Guild) references Guilds(ID_Guild)
);

create table Text_Channels(
    ID_Text char(18),
    ID_Guild char(18),
    Text_name varchar(75),
    primary key(ID_Text, ID_Guild, Text_name),
    foreign key(ID_Guild) references Guilds(ID_Guild)
);
create table ComandosVoz(
    Comando varchar(50),
    Duracao float,
    primary key(Comando, Duracao)
);

create table ComandosTexto(
	Comando varchar(50),
    primary key(Comando)
);

create table UsoComandosVoz(
	ID_Usuario char(18),
    ID_Guild char(18),
    ID_VC char(18),
    ID_Text char(18),
    MomentoUso datetime,
    Comando varchar(50),
	Quantidade int,
    primary key(ID_Usuario, ID_Guild, ID_VC, ID_Text, MomentoUso, Comando, Quantidade),
    foreign key (Comando) references ComandosVoz(Comando),
    foreign key (ID_Usuario) references Usuarios(ID_Usuario),
    foreign key (ID_Guild) references Guilds(ID_Guild),
    foreign key (ID_VC) references Voice_Channels(ID_VC),
    foreign key (ID_Text) references Text_Channels(ID_Text)
);

create table UsoComandosTexto(
	ID_Usuario char(18),
    ID_Guild char(18),
    ID_Text char(18),
    MomentoUso datetime,
    Comando varchar(50),
	Quantidade int,
    primary key(ID_Usuario, ID_Guild, ID_Text, MomentoUso, Comando, Quantidade),
    foreign key (Comando) references ComandosTexto(Comando),
    foreign key (ID_Usuario) references Usuarios(ID_Usuario),
    foreign key (ID_Guild) references Guilds(ID_Guild),
    foreign key (ID_Text) references Text_Channels(ID_Text)
);
