#!/usr/bin/env python3
from collections import Counter
from pathlib import Path
import json, math, re
ROOT=Path(__file__).resolve().parent
TOKEN=re.compile(r"[a-z0-9]+")
STOP={"a","an","and","are","as","at","be","before","can","does","for","from","how","in","is","it","of","on","or","the","to","what","when","which","who"}
def tokens(text): return [t for t in TOKEN.findall(text.lower()) if t not in STOP]
def main():
    corpus=json.loads((ROOT/"corpus.json").read_text())["passages"]
    questions=json.loads((ROOT/"questions.json").read_text())["questions"]
    docs=[tokens(" ".join([p["document"],p["type"],p["text"]])) for p in corpus]
    avgdl=sum(map(len,docs))/len(docs); df=Counter(t for d in docs for t in set(d)); n=len(docs)
    def rank(query):
        q=Counter(tokens(query)); scored=[]
        for passage,doc in zip(corpus,docs):
            tf=Counter(doc); score=0.0
            for term,qtf in q.items():
                if term not in tf: continue
                idf=math.log(1+(n-df[term]+.5)/(df[term]+.5)); denom=tf[term]+1.5*(.25+.75*len(doc)/avgdl)
                score+=qtf*idf*tf[term]*2.5/denom
            scored.append({"id":passage["id"],"score":round(score,6)})
        return sorted(scored,key=lambda x:(-x["score"],x["id"]))[:5]
    results=[]; reciprocal=[]; hit1=hit5=0
    for question in questions:
        ranked=rank(question["query"]); expected=set(question["expected"])
        if not expected: rank_value=None; passed=False
        else:
            positions=[i+1 for i,row in enumerate(ranked) if row["id"] in expected]; rank_value=min(positions) if positions else None; passed=rank_value is not None
            if rank_value==1: hit1+=1
            if passed: hit5+=1; reciprocal.append(1/rank_value)
            else: reciprocal.append(0)
        results.append({**question,"rank":rank_value,"pass_at_5":passed,"returned":ranked})
    answerable=sum(bool(q["expected"]) for q in questions)
    report={"benchmark_version":"2026-08-12","method":"dependency-free BM25-style lexical retrieval","question_count":len(questions),"answerable_question_count":answerable,"metrics":{"hit_at_1":round(hit1/answerable,4),"hit_at_5":round(hit5/answerable,4),"mrr":round(sum(reciprocal)/answerable,4)},"results":results}
    (ROOT/"baseline-report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report["metrics"],indent=2)); failures=[r for r in results if not r["pass_at_5"]]; print(f"documented_failures={len(failures)}")
    for row in failures: print(f"{row['id']} {row['category']}: {row['query']}")
if __name__=="__main__": main()
