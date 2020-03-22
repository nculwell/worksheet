.mode csv
select vpi.infinitive
, vpi
from verbs vpi
left join verbs vps on vps.infinitive = vpi.infinitive and vps.mood = 'Subjuntivo' and vps.tense = 'Presente'
left join verbs vti on vps.infinitive = vpi.infinitive and vps.mood = 'Indicativo' and vps.tense = 'Pretérito'
left join verbs vts on vps.infinitive = vpi.infinitive and vps.mood = 'Subjuntivo' and vps.tense = 'Pretérito'
where vpi.mood = 'Indicativo' and vpi.tense = 'Presente'
/*
--MOOD
Imperativo Afirmativo
Imperativo Negativo
Indicativo
Subjuntivo
--TENSE
Condicional
Condicional perfecto
Futuro
Futuro perfecto
Imperfecto
Pluscuamperfecto
Presente
Presente perfecto
Pretérito
Pretérito anterior
*/
/*
CREATE TABLE gerund (
  infinitive character varying NOT NULL primary key,
  gerund character varying NOT NULL,
  gerund_english character varying
);
CREATE TABLE infinitive (
  infinitive character varying NOT NULL primary key,
  infinitive_english character varying
);
CREATE TABLE mood (
  mood character varying NOT NULL primary key,
  mood_english character varying
);
CREATE TABLE pastparticiple (
  infinitive character varying NOT NULL primary key,
  pastparticiple character varying NOT NULL,
  pastparticiple_english character varying
);
CREATE TABLE tense (
  tense character varying NOT NULL primary key,
  tense_english character varying
);
CREATE TABLE verbs (
  infinitive character varying NOT NULL,
  mood character varying NOT NULL,
  tense character varying NOT NULL,
  verb_english character varying,
  form_1s character varying,
  form_2s character varying,
  form_3s character varying,
  form_1p character varying,
  form_2p character varying,
  form_3p character varying,
  PRIMARY KEY (infinitive, mood, tense)
);
*/

