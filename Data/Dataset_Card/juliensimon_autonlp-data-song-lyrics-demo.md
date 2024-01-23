---
language:
- en
task_categories:
- text-classification
---
# AutoNLP Dataset for project: song-lyrics-demo

## Table of content
- [Dataset Description](#dataset-description)
    - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)

## Dataset Descritpion

This dataset has been automatically processed by AutoNLP for project song-lyrics-demo.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "target": 2,
    "text": "[Intro: Method Man w/ sample] + (Sunny valentine). We got butter (8X). (The gun'll go the gun'll go.... The gun'll go...). [Raekwon]. Aiyo one thing for sure keep you of all. Keep a nice crib fly away keep to the point. Keep niggaz outta ya face who snakes. Keep bitches in they place keep the mac in a special place. Keep moving for papes keep cool keep doing what you doing. Keep it fly keep me in the crates. Cuz I will erase shit on the real note you'se a waste. It's right here for you I will lace you. Rip you and brace you put a nice W up on ya face. Word to mother you could get chased. It's nothing to taste blood on a thug if he gotta go. All I know is we be giving grace. This is a place from where we make tapes. We make 'em everywhere still in all we be making base. Y'all be making paste these little niggaz they be making shapes. Our shit is art yours is traced. [Chorus: Sunny Valentine]. This is the way that we rolling in the streets. You know when we roll we be packing that heat. The gun'll go the gun'll go the gun'll go the gun'll go. The gun'll go the gun'll go the gun'll go the gun'll go. The gun'll go the gun'll go.... [Method Man]. This is Poverty Island man these animals don't run. Slums where the ambulance don't come. Who got the best base? Fiends waiting to smoke some. Approach something ask him where he getting that coke from. My dudes hug blocks like samurai shogun. Cuz no V and no ones equalling no fun. Who want a treat they know huh? Body to go numb. My woman need funds plus her hair and her toes done. It is what it is though you fuck with the kid flow. That make it hard to get dough the harder to get gold. Harder the piff blow harder when it snow. The pinky and the wrist glow this here what we live for. Get gwop then get low but first thought. We gotta get the work off the gift and the curse boss. Yeah see I'm the shit yo the dirt in the fit no. Hustling from the get-go the motto is get more. [Chorus]. [Masta Killa]. We was quiet flashy brothers strapped all along. With the dirty .38 long twelve hour shift gate. Took case state to state you think he won't hold his weight?. Put ya money on the plate and watch it get scrapped. We get ape up in that club off that juice and Henn. And it's a no win situation fucking with them. You mean like Ewing at the front at the rim finger roll a Dutch. Million dollar stages touched techs gauges bust. Trust no one the lone shogun rugged Timb boot stomper. Damaging lyrical mass destruction launcher. Nothing can calm the quakeage when I break kid. Peace to my brothers up north doing state bids. [Chorus]. [Chorus 2: Sunny Valentine]. Whoa... this is the way we be rolling in the club. You know when we roll we be packing .32 snubs. The gun'll go the gun'll go the gun'll go the gun'll go. The gun'll go the gun'll go the gun'll go the gun'll go. The gun'll go the gun'll go the gun'll go the gun'll go. [Outro: sample to fade]. We got butter..."
  },
  {
    "target": 4,
    "text": "[Sean Paul:]. Aye. It's Sean Paul 'long side. The mandem called Jay Sean. Fi di gal dem. Tellin' 'em again what we tell 'em. [Jay Sean:]. Pass me a drink to the left yeah. Said her name was Delilah. And I'm like \"you should come my way\". I already surrender. Damn girl that body's fire. You gon' remember my name. (She should give it up definite). You need it. I need it. We can jump in the deep end. I wanna get lost in your love. I just wanna be close to you. (Just wanna I just wanna). And do all the things you want me to. I just wanna be close to you. (I just wanna I just wanna). And show you the way I feel. You make my love go. You make my love go. You make my love go. In the morning we gon' do it again wake up. I'mma do it like we just broke up and made up. Get up on top of me and work up a sweat work up a sweat. See we can do it any type of way that you want. I'm thinking maybe you're the right kind of wrong. I'm saying baby you won't ever forget my love. You need it. I need it. We can jump in the deep end. I wanna get lost in your love. I just wanna be close to you. (Just wanna I just wanna). And do all the things you want me to. I just wanna be close to you. (I just wanna I just wanna). And show you the way I feel. You make my love go. You make my love go. You make my love go. [Sean Paul:]. Girl mi wan' figure hundred hundred and fifty. Love how you move you know that I'm with it. Perfect size I know that you fit it. Just let me hit it you know mi not quit it. Pon di Dl like Cassie and Diddy. Mi na wound a mi watch we like Sin City. Full time mi run da ting mi tall legend. If you don't come gimme dat would I be offended my girl. Come here down wan' see something me want in life and then waste time. A you a mi pree every day baby full time when ya de pon on mi mind. So mi wine if you give it to me baby girl so we can play. Stick to the ting now I am your king my girl this is what we say. [Jay Sean:]. I just wanna be close to you. (Just wanna I just wanna). And do all the things you want me to. I just wanna be close to you. (I just wanna I just wanna). And show you the way I feel. You make my love go. You make my love go. You make my love go"
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "target": "ClassLabel(num_classes=6, names=['Dance', 'Heavy Metal', 'Hip Hop', 'Indie', 'Pop', 'Rock'], names_file=None, id=None)",
  "text": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 48493 |
| valid        | 5389 |
