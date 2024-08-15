(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[36209],{882689:(t,e,i)=>{var l=i(829932),n=i(297786),s=i(267206),o=i(269199),r=i(571131),c=i(307518),u=i(285022),a=i(406557),d=i(701469);t.exports=function(t,e,i){e=e.length?l(e,(function(t){return d(t)?function(e){return n(e,1===t.length?t[0]:t)}:t})):[a];var f=-1;e=l(e,c(s));var v=o(t,(function(t,i,n){return{criteria:l(e,(function(e){return e(t)})),index:++f,value:t}}));return r(v,(function(t,e){return u(t,e,i)}))}},571131:t=>{t.exports=function(t,e){var i=t.length;for(t.sort(e);i--;)t[i]=t[i].value;return t}},626393:(t,e,i)=>{var l=i(733448);t.exports=function(t,e){if(t!==e){var i=void 0!==t,n=null===t,s=t===t,o=l(t),r=void 0!==e,c=null===e,u=e===e,a=l(e);if(!c&&!a&&!o&&t>e||o&&r&&u&&!c&&!a||n&&r&&u||!i&&u||!s)return 1;if(!n&&!o&&!a&&t<e||a&&i&&s&&!n&&!o||c&&i&&s||!r&&s||!u)return-1}return 0}},285022:(t,e,i)=>{var l=i(626393);t.exports=function(t,e,i){for(var n=-1,s=t.criteria,o=e.criteria,r=s.length,c=i.length;++n<r;){var u=l(s[n],o[n]);if(u)return n>=c?u:u*("desc"==i[n]?-1:1)}return t.index-e.index}},875472:(t,e,i)=>{var l=i(882689),n=i(701469);t.exports=function(t,e,i,s){return null==t?[]:(n(e)||(e=null==e?[]:[e]),n(i=s?void 0:i)||(i=null==i?[]:[i]),l(t,e,i))}},936209:(t,e,i)=>{"use strict";i.r(e),i.d(e,{default:()=>w});var l=i(875472),n=i.n(l),s=i(607739),o=i.n(s),r=i(667294),c=i(751995),u=i(211965),a=i(885673),d=i(412556);const f=30,v=c.iK.div`
  height: ${f}px;
  width: 100%;
  display: flex;
  cursor: pointer;
`,h=c.iK.div`
  height: 100%;
  display: flex;
  overflow: hidden;
  white-space: nowrap;
  align-items: center;
  justify-content: center;
`,g=c.iK.div`
  text-overflow: ellipsis;
  overflow: hidden;
`,p=c.iK.div`
  width: 100%;
  height: 100%;
  position: relative;
  display: flex;
  align-items: center;
`,x=c.iK.div`
  width: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
`,y=c.iK.div``;function w(t){const{height:e,width:i,data:l=[],formData:s}=t,[c,w]=(0,r.useState)(""),[Z,b]=(0,r.useState)("");if(0===l.length)return(0,u.tZ)("div",{style:{position:"relative",width:i,height:e,display:"flex",alignItems:"center",justifyContent:"center",fontSize:20,fontWeight:600}},"\u6682\u65e0\u6570\u636e");const{rowDimension:$,columnDimensionAndcorrelation:m,correlationValue:k}=s,j=o()(l,$),K=o()(l,m);let C=Object.values(j);const D=Object.values(K),S=[],T=[];D.forEach((t=>{const e=t.every((t=>null===(null==t?void 0:t[k])||(null==t?void 0:t[k])<1)),i=t.every((t=>0===(null==t?void 0:t[k])));var l;e&&!i?(S.unshift(t),T.push(null==t||null==(l=t[0])?void 0:l[m])):S.push(t)})),(0,r.useEffect)((()=>{T.length>0&&(w("desc"),b(T[0]))}),[JSON.stringify(T)]);const E=C.length+1,O=D.length+1,z=[],A=i/O;for(let t=0;t<E;t++){const e=[];for(let i=0;i<O;i++){var N,q,F,I;let s=`${t}-${i}`;const o=null==(N=S[i-1])||null==(q=N[0])?void 0:q[m];if(c&&T.includes(Z)&&Z===o){let t=[];for(let e=0;e<S.length;e++){var J;const i=S[e];if((null==i||null==(J=i[0])?void 0:J[m])===Z){t=n()(i,[k],[c]);break}}const e=[];let i=C;t.forEach((t=>{const l=C.filter((e=>{var i;return(null==e||null==(i=e[0])?void 0:i[$])===(null==t?void 0:t[$])}));l.length&&e.push(l[0]),i=i.filter((e=>{var i;return(null==e||null==(i=e[0])?void 0:i[$])!==(null==t?void 0:t[$])}))}));const l=[...e,...i];C.length===l.length&&(C=l)}const r=null==(F=C[t-1])||null==(I=F[0])?void 0:I[$];if(0===t)if(0===i){const t=`(N=${l.length})`;s=(0,u.tZ)(g,{css:u.iv`
                font-style: oblique;
                display: flex;
                align-items: center;
                justify-content: flex-start;
                color: #999;
                width: 100%;
              `,title:t},`${t}`)}else s=(0,u.tZ)(g,{css:u.iv`
                font-size: 16px;
                font-weight: 600;
              `,title:o},o);else if(0===i)s=(0,u.tZ)(g,null,r);else{var M;const t=l.filter((t=>(null==t?void 0:t[m])===o&&t[$]===r));let e=null==t||null==(M=t[0])?void 0:M[k];if(T.includes(o)){const t=100*Math.abs(e),i=e>0?"#15A933":"#FC0006";s=(0,u.tZ)(p,{css:u.iv`
                display: flex;
                align-items: center;
                justify-content: center;
              `},(0,u.tZ)(x,{css:u.iv`
                  justify-content: flex-end;
                `},e<0&&(0,u.tZ)(y,{css:u.iv`
                      width: 100%;
                      display: flex;
                      align-items: center;
                      position: relative;
                    `},(0,u.tZ)(y,{css:u.iv`
                        width: calc(100% - ${t}%);
                        height: 18px;
                      `}),(0,u.tZ)(y,{css:u.iv`
                        width: ${t}%;
                        height: 18px;
                        background-color: ${i};
                      `}),(0,u.tZ)(y,{css:u.iv`
                        position: absolute;
                        right: 0;
                      `},e))),(0,u.tZ)(x,{css:u.iv`
                  justify-content: flex-start;
                `},e>=0&&(0,u.tZ)(y,{css:u.iv`
                      width: 100%;
                      display: flex;
                      align-items: center;
                      position: relative;
                    `},(0,u.tZ)(y,{css:u.iv`
                        width: ${t}%;
                        height: 18px;
                        background-color: ${i};
                      `}),(0,u.tZ)(y,{css:u.iv`
                        position: absolute;
                      `},e))))}else s=(0,u.tZ)(p,null,(0,u.tZ)(y,{css:u.iv`
                  width: ${e||0}%;
                  background-color: #95cfff;
                `},null!==e&&void 0!==e?`${e}%`:""))}const f=T.includes(o);let v="";f&&(v=0===t?"#515151":"rgba(0, 0, 0, 0.05)"),e.push((0,u.tZ)(h,{css:u.iv`
            width: ${A}px;
            background-color: ${v};
            color: ${f&&0===t?"#fff":""};
          `,onClick:()=>{f&&0===t&&("asc"===c?(w("desc"),b(o)):"desc"===c?(w(""),b("")):(w("asc"),b(o)))}},s,f&&0===t&&(0,u.tZ)("div",{style:{display:"flex",flexDirection:"column"}},(0,u.tZ)(a.default,{style:"asc"===c?{color:"#1890ff"}:{}}),(0,u.tZ)(d.default,{style:"desc"===c?{color:"#1890ff",marginTop:-5}:{marginTop:-5}}))))}const i=(0,u.tZ)(v,{css:u.iv`
          background-color: ${t%2===1?"#eee":""};
        `},e);z.push(i)}return(0,u.tZ)("div",{style:{position:"relative",width:i,height:e}},(null==z||null==z.slice?void 0:z.slice(0,1))||null,(0,u.tZ)("div",{style:{position:"relative",width:i,height:e-f,overflow:"scroll"}},(null==z||null==z.slice?void 0:z.slice(1))||null))}}}]);