from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
from autocorrect import Speller

app = FastAPI()

data_sets = {"10%":2,"2021":1,"2022":1,"3":8,"3month":2,"4":2,"5%":1,"6":6,"8":1,"9%":1,"Fi":1,"I":1,"a":59,"acc":2,"account":60,"accounts":3,"add":4,"agent":99,"agents":6,"all":3,"am":1,"an":15,"and":4,"app":3,"applied":2,"apply":54,"applying":4,"asap":1,"ask":1,"atm":4,"aug":1,"avail":2,"back":1,"balance":1,"bamking":1,"bank":90,"banking":2,"benefits":1,"best":1,"book":132,"book?":2,"books":2,"call":44,"calling":1,"camn":1,"can":100,"cancel":9,"cancelled":1,"card":18,"cards":1,"care":100,"cc":2,"cear":1,"centre":2,"charges":1,"chat":23,"chat?":1,"check":7,"checking":1,"cheque":175,"chequebook":35,"chequebook?":1,"cheques":4,"close":2,"closure":1,"code":2,"collect":2,"complaint":1,"connect":13,"connecting":1,"contact":95,"costumer":1,"could":1,"cre":1,"create":2,"credit":10,"customer":162,"customercare":3,"customercontact":1,"customers":5,"customised":1,"date":1,"day":1,"debit":1,"december":1,"delivery":1,"deposit":6,"deposits":8,"detail":1,"details":1,"direct":1,"do":22,"does":2,"download":35,"e":3,"earn":2,"email":1,"emergency":1,"epf":7,"executive":3,"federal":5,"feedback":1,"fees":1,"fi":97,"fii":1,"file":3,"fimony":1,"financial":3,"find":7,"fine":1,"fixed":4,"for":42,"forgot":3,"free":4,"from":1,"full":2,"fund":3,"funds":3,"generate":2,"genrate":1,"get":113,"give":9,"go":2,"got":1,"have":4,"help":6,"helping":1,"helpline":1,"how":323,"i":264,"id":1,"ifsc":2,"in":9,"interest":2,"internet":1,"invest":4,"invested":1,"investment":2,"investments":6,"is":12,"issue":1,"issues":1,"iwant":1,"jump":6,"june2022":1,"just":2,"know":1,"kyc":5,"l":2,"last":12,"leaf":5,"like":1,"line":2,"live":3,"loan":3,"loans":1,"locate":1,"location":1,"mail":6,"make":2,"march":1,"march2022":1,"me":23,"mf":1,"mi":1,"mini":7,"ministatement":1,"mobile":3,"money":8,"month":14,"monthly":1,"months":10,"much":1,"mutual":5,"my":125,"need":16,"net":5,"netbanking":1,"networth":3,"new":2,"no":13,"no.":2,"nook":1,"now":1,"numbe":1,"number":63,"number?":1,"numbers":2,"oder":1,"of":13,"offer":2,"offers":3,"office":1,"officer":4,"officers":1,"official":1,"on":7,"one":3,"online":3,"open":5,"order":30,"ordered":1,"ordering":1,"outstanding":2,"p2p":1,"pass":1,"passbook":1,"pay":1,"pdf":6,"personal":1,"phone":3,"pin":6,"place":3,"please":14,"problem":3,"qr":3,"query":1,"r":1,"receive":1,"received":1,"recharge":2,"regarding":2,"relationship":1,"request":43,"requestcall":1,"requesting":2,"requests":1,"required":1,"rewards":2,"ro":1,"salary":7,"saving":1,"savings":2,"scan":3,"score":2,"see":7,"send":9,"service":26,"setting":1,"settings":1,"should":1,"show":12,"shut":2,"sir":1,"smart":6,"solve":1,"speak":5,"statement":210,"statement?":4,"statementm":1,"statements":24,"status":3,"submit":1,"support":18,"suuport":1,"take":9,"talk":36,"team":3,"the":26,"this":4,"three":2,"threemonths":1,"through":1,"till":1,"to":253,"to.apply":1,"toll":1,"total":1,"tp":1,"track":2,"transaction":3,"transactions":1,"txns":2,"u":1,"unable":1,"up":1,"upi":4,"upi_id":1,"urgent":1,"urgently":2,"us":2,"use":1,"value":2,"valueback":3,"video":1,"videokyc":1,"view":1,"wann":1,"wanna":1,"want":113,"wanted":2,"we":3,"what":7,"where":12,"will":7,"wish":1,"with":50,"withdraw":1,"worth":4,"would":1,"year":4,"yearly":1,"yo":1,"you":3,"your":6}

spell = Speller(nlp_data= data_sets)

class TextRequest(BaseModel):
    text: str

@app.post("/suggest")
def suggest_word(request: TextRequest):
    input_text = request.text
    try:
        # Generate suggestions
        suggestions = spell(input_text)
        return {"suggestions": suggestions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)