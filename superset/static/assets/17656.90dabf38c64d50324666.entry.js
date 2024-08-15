(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[17656],{357179:(e,t,a)=>{"use strict";a.d(t,{$:()=>n});var r=a(607739),o=a.n(r);const n=(e,t,a,r,n,s="name")=>{const i=(e,t)=>{const a=e[t],r=`${a}_${t}`;return{...e,title:a,key:r,nodeType:t}},l=(e,n)=>Object.keys(e).map((c=>{const d=e[c].map((e=>i(e,n))),u=d[0];if(t.indexOf(n)+1<t.length){const e=t[t.indexOf(n)+1],a=o()(d,e);return{...u,children:l(Object.values(a),e),disabled:!0}}const h=t.length-1,p=u[t[h]],m=r.filter((e=>(null==e?void 0:e[s])===p))||[];return m.length>0?{...u,...m[0],title:null==a?void 0:a(m[0])}:{...u,title:null==a?void 0:a(u)}})),c=t[0],d=o()(e,c),u=l(d,c);if(n){const t=e.map((e=>e.field_code))||[],o=r.filter((e=>!t.includes(e.column_name))).map((e=>{const t=i(e,"column_name");return{...t,title:null==a?void 0:a(t)}}));u.push({key:"uni_other",title:"\u5176\u4ed6\u5206\u7ec4",disabled:!0,children:[{key:"uni_other_sencod",title:"\u5176\u4ed6\u5206\u7ec4",disabled:!0,children:o}]})}return u}},690233:(e,t,a)=>{"use strict";a.d(t,{Lu:()=>l,tL:()=>s});var r=a(722122),o=a(376826),n=a.n(o),s={CASE_SENSITIVE_EQUAL:7,EQUAL:6,STARTS_WITH:5,WORD_STARTS_WITH:4,CONTAINS:3,ACRONYM:2,MATCHES:1,NO_MATCH:0};l.rankings=s;var i=function(e,t){return String(e.rankedValue).localeCompare(String(t.rankedValue))};function l(e,t,a){void 0===a&&(a={});var o=a,n=o.keys,l=o.threshold,d=void 0===l?s.MATCHES:l,h=o.baseSort,m=void 0===h?i:h,g=o.sorter,f=void 0===g?function(e){return e.sort((function(e,t){return function(e,t,a){var r=-1,o=1,n=e.rank,s=e.keyIndex,i=t.rank,l=t.keyIndex;return n===i?s===l?a(e,t):s<l?r:o:n>i?r:o}(e,t,m)}))}:g,v=e.reduce((function(e,o,i){var l=function(e,t,a,r){if(!t){return{rankedValue:e,rank:c(e,a,r),keyIndex:-1,keyThreshold:r.threshold}}var o=function(e,t){for(var a=[],r=0,o=t.length;r<o;r++)for(var n=t[r],s=p(n),i=u(e,n),l=0,c=i.length;l<c;l++)a.push({itemValue:i[l],attributes:s});return a}(e,t);return o.reduce((function(e,t,o){var n=e.rank,i=e.rankedValue,l=e.keyIndex,d=e.keyThreshold,u=t.itemValue,h=t.attributes,p=c(u,a,r),m=i,g=h.minRanking,f=h.maxRanking,v=h.threshold;return p<g&&p>=s.MATCHES?p=g:p>f&&(p=f),p>n&&(n=p,l=o,d=v,m=u),{rankedValue:m,rank:n,keyIndex:l,keyThreshold:d}}),{rankedValue:e,rank:s.NO_MATCH,keyIndex:-1,keyThreshold:r.threshold})}(o,n,t,a),h=l.rank,m=l.keyThreshold;h>=(void 0===m?d:m)&&e.push((0,r.Z)({},l,{item:o,index:i}));return e}),[]);return f(v).map((function(e){return e.item}))}function c(e,t,a){return e=d(e,a),(t=d(t,a)).length>e.length?s.NO_MATCH:e===t?s.CASE_SENSITIVE_EQUAL:(e=e.toLowerCase())===(t=t.toLowerCase())?s.EQUAL:e.startsWith(t)?s.STARTS_WITH:e.includes(" "+t)?s.WORD_STARTS_WITH:e.includes(t)?s.CONTAINS:1===t.length?s.NO_MATCH:(r=e,o="",r.split(" ").forEach((function(e){e.split("-").forEach((function(e){o+=e.substr(0,1)}))})),o).includes(t)?s.ACRONYM:function(e,t){var a=0,r=0;function o(e,t,r){for(var o=r,n=t.length;o<n;o++){if(t[o]===e)return a+=1,o+1}return-1}function n(e){var r=1/e,o=a/t.length;return s.MATCHES+o*r}var i=o(t[0],e,0);if(i<0)return s.NO_MATCH;r=i;for(var l=1,c=t.length;l<c;l++){if(!((r=o(t[l],e,r))>-1))return s.NO_MATCH}return n(r-i)}(e,t);var r,o}function d(e,t){return e=""+e,t.keepDiacritics||(e=n()(e)),e}function u(e,t){var a;if("object"===typeof t&&(t=t.key),"function"===typeof t)a=t(e);else if(null==e)a=null;else if(Object.hasOwnProperty.call(e,t))a=e[t];else{if(t.includes("."))return function(e,t){for(var a=e.split("."),r=[t],o=0,n=a.length;o<n;o++){for(var s=a[o],i=[],l=0,c=r.length;l<c;l++){var d=r[l];if(null!=d)if(Object.hasOwnProperty.call(d,s)){var u=d[s];null!=u&&i.push(u)}else"*"===s&&(i=i.concat(d))}r=i}if(Array.isArray(r[0])){var h=[];return h.concat.apply(h,r)}return r}(t,e);a=null}return null==a?[]:Array.isArray(a)?a:[String(a)]}var h={maxRanking:1/0,minRanking:-1/0};function p(e){return"string"===typeof e?h:(0,r.Z)({},h,e)}},376826:e=>{var t={\u00c0:"A",\u00c1:"A",\u00c2:"A",\u00c3:"A",\u00c4:"A",\u00c5:"A",\u1ea4:"A",\u1eae:"A",\u1eb2:"A",\u1eb4:"A",\u1eb6:"A",\u00c6:"AE",\u1ea6:"A",\u1eb0:"A",\u0202:"A",\u00c7:"C",\u1e08:"C",\u00c8:"E",\u00c9:"E",\u00ca:"E",\u00cb:"E",\u1ebe:"E",\u1e16:"E",\u1ec0:"E",\u1e14:"E",\u1e1c:"E",\u0206:"E",\u00cc:"I",\u00cd:"I",\u00ce:"I",\u00cf:"I",\u1e2e:"I",\u020a:"I",\u00d0:"D",\u00d1:"N",\u00d2:"O",\u00d3:"O",\u00d4:"O",\u00d5:"O",\u00d6:"O",\u00d8:"O",\u1ed0:"O",\u1e4c:"O",\u1e52:"O",\u020e:"O",\u00d9:"U",\u00da:"U",\u00db:"U",\u00dc:"U",\u00dd:"Y",\u00e0:"a",\u00e1:"a",\u00e2:"a",\u00e3:"a",\u00e4:"a",\u00e5:"a",\u1ea5:"a",\u1eaf:"a",\u1eb3:"a",\u1eb5:"a",\u1eb7:"a",\u00e6:"ae",\u1ea7:"a",\u1eb1:"a",\u0203:"a",\u00e7:"c",\u1e09:"c",\u00e8:"e",\u00e9:"e",\u00ea:"e",\u00eb:"e",\u1ebf:"e",\u1e17:"e",\u1ec1:"e",\u1e15:"e",\u1e1d:"e",\u0207:"e",\u00ec:"i",\u00ed:"i",\u00ee:"i",\u00ef:"i",\u1e2f:"i",\u020b:"i",\u00f0:"d",\u00f1:"n",\u00f2:"o",\u00f3:"o",\u00f4:"o",\u00f5:"o",\u00f6:"o",\u00f8:"o",\u1ed1:"o",\u1e4d:"o",\u1e53:"o",\u020f:"o",\u00f9:"u",\u00fa:"u",\u00fb:"u",\u00fc:"u",\u00fd:"y",\u00ff:"y",\u0100:"A",\u0101:"a",\u0102:"A",\u0103:"a",\u0104:"A",\u0105:"a",\u0106:"C",\u0107:"c",\u0108:"C",\u0109:"c",\u010a:"C",\u010b:"c",\u010c:"C",\u010d:"c",C\u0306:"C",c\u0306:"c",\u010e:"D",\u010f:"d",\u0110:"D",\u0111:"d",\u0112:"E",\u0113:"e",\u0114:"E",\u0115:"e",\u0116:"E",\u0117:"e",\u0118:"E",\u0119:"e",\u011a:"E",\u011b:"e",\u011c:"G",\u01f4:"G",\u011d:"g",\u01f5:"g",\u011e:"G",\u011f:"g",\u0120:"G",\u0121:"g",\u0122:"G",\u0123:"g",\u0124:"H",\u0125:"h",\u0126:"H",\u0127:"h",\u1e2a:"H",\u1e2b:"h",\u0128:"I",\u0129:"i",\u012a:"I",\u012b:"i",\u012c:"I",\u012d:"i",\u012e:"I",\u012f:"i",\u0130:"I",\u0131:"i",\u0132:"IJ",\u0133:"ij",\u0134:"J",\u0135:"j",\u0136:"K",\u0137:"k",\u1e30:"K",\u1e31:"k",K\u0306:"K",k\u0306:"k",\u0139:"L",\u013a:"l",\u013b:"L",\u013c:"l",\u013d:"L",\u013e:"l",\u013f:"L",\u0140:"l",\u0141:"l",\u0142:"l",\u1e3e:"M",\u1e3f:"m",M\u0306:"M",m\u0306:"m",\u0143:"N",\u0144:"n",\u0145:"N",\u0146:"n",\u0147:"N",\u0148:"n",\u0149:"n",N\u0306:"N",n\u0306:"n",\u014c:"O",\u014d:"o",\u014e:"O",\u014f:"o",\u0150:"O",\u0151:"o",\u0152:"OE",\u0153:"oe",P\u0306:"P",p\u0306:"p",\u0154:"R",\u0155:"r",\u0156:"R",\u0157:"r",\u0158:"R",\u0159:"r",R\u0306:"R",r\u0306:"r",\u0212:"R",\u0213:"r",\u015a:"S",\u015b:"s",\u015c:"S",\u015d:"s",\u015e:"S",\u0218:"S",\u0219:"s",\u015f:"s",\u0160:"S",\u0161:"s",\u0162:"T",\u0163:"t",\u021b:"t",\u021a:"T",\u0164:"T",\u0165:"t",\u0166:"T",\u0167:"t",T\u0306:"T",t\u0306:"t",\u0168:"U",\u0169:"u",\u016a:"U",\u016b:"u",\u016c:"U",\u016d:"u",\u016e:"U",\u016f:"u",\u0170:"U",\u0171:"u",\u0172:"U",\u0173:"u",\u0216:"U",\u0217:"u",V\u0306:"V",v\u0306:"v",\u0174:"W",\u0175:"w",\u1e82:"W",\u1e83:"w",X\u0306:"X",x\u0306:"x",\u0176:"Y",\u0177:"y",\u0178:"Y",Y\u0306:"Y",y\u0306:"y",\u0179:"Z",\u017a:"z",\u017b:"Z",\u017c:"z",\u017d:"Z",\u017e:"z",\u017f:"s",\u0192:"f",\u01a0:"O",\u01a1:"o",\u01af:"U",\u01b0:"u",\u01cd:"A",\u01ce:"a",\u01cf:"I",\u01d0:"i",\u01d1:"O",\u01d2:"o",\u01d3:"U",\u01d4:"u",\u01d5:"U",\u01d6:"u",\u01d7:"U",\u01d8:"u",\u01d9:"U",\u01da:"u",\u01db:"U",\u01dc:"u",\u1ee8:"U",\u1ee9:"u",\u1e78:"U",\u1e79:"u",\u01fa:"A",\u01fb:"a",\u01fc:"AE",\u01fd:"ae",\u01fe:"O",\u01ff:"o",\u00de:"TH",\u00fe:"th",\u1e54:"P",\u1e55:"p",\u1e64:"S",\u1e65:"s",X\u0301:"X",x\u0301:"x",\u0403:"\u0413",\u0453:"\u0433",\u040c:"\u041a",\u045c:"\u043a",A\u030b:"A",a\u030b:"a",E\u030b:"E",e\u030b:"e",I\u030b:"I",i\u030b:"i",\u01f8:"N",\u01f9:"n",\u1ed2:"O",\u1ed3:"o",\u1e50:"O",\u1e51:"o",\u1eea:"U",\u1eeb:"u",\u1e80:"W",\u1e81:"w",\u1ef2:"Y",\u1ef3:"y",\u0200:"A",\u0201:"a",\u0204:"E",\u0205:"e",\u0208:"I",\u0209:"i",\u020c:"O",\u020d:"o",\u0210:"R",\u0211:"r",\u0214:"U",\u0215:"u",B\u030c:"B",b\u030c:"b",\u010c\u0323:"C",\u010d\u0323:"c",\u00ca\u030c:"E",\u00ea\u030c:"e",F\u030c:"F",f\u030c:"f",\u01e6:"G",\u01e7:"g",\u021e:"H",\u021f:"h",J\u030c:"J",\u01f0:"j",\u01e8:"K",\u01e9:"k",M\u030c:"M",m\u030c:"m",P\u030c:"P",p\u030c:"p",Q\u030c:"Q",q\u030c:"q",\u0158\u0329:"R",\u0159\u0329:"r",\u1e66:"S",\u1e67:"s",V\u030c:"V",v\u030c:"v",W\u030c:"W",w\u030c:"w",X\u030c:"X",x\u030c:"x",Y\u030c:"Y",y\u030c:"y",A\u0327:"A",a\u0327:"a",B\u0327:"B",b\u0327:"b",\u1e10:"D",\u1e11:"d",\u0228:"E",\u0229:"e",\u0190\u0327:"E",\u025b\u0327:"e",\u1e28:"H",\u1e29:"h",I\u0327:"I",i\u0327:"i",\u0197\u0327:"I",\u0268\u0327:"i",M\u0327:"M",m\u0327:"m",O\u0327:"O",o\u0327:"o",Q\u0327:"Q",q\u0327:"q",U\u0327:"U",u\u0327:"u",X\u0327:"X",x\u0327:"x",Z\u0327:"Z",z\u0327:"z"},a=Object.keys(t).join("|"),r=new RegExp(a,"g"),o=new RegExp(a,""),n=function(e){return e.replace(r,(function(e){return t[e]}))};e.exports=n,e.exports.has=function(e){return!!e.match(o)},e.exports.remove=n},888154:(e,t,a)=>{"use strict";a.d(t,{Z:()=>l});var r=a(205872),o=a.n(r),n=a(667294),s=a(970553),i=a(211965);const l=({onChange:e,treeData:t=[],allowNewOptions:a,...r})=>{const[l,c]=(0,n.useState)(""),[d,u]=(0,n.useState)([]),[h,p]=(0,n.useState)([]),m=(e,t)=>{const a=e.indexOf(t),r=e.substr(0,a),o=e.substr(a+t.length);return a>-1?(0,i.tZ)("span",{"test-data":e,style:{color:"#000"}},r,(0,i.tZ)("span",{style:{color:"#f50"}},t),o):(0,i.tZ)("span",{"test-data":e,style:{color:"#000"}},e)},g=(e=[],t,a=!1)=>{if(!e||!t)return e;const r=[];return e.forEach((e=>{e.title.includes(t)?r.push({...e,title:m(e.title,t),children:g(e.children,t,!0)}):e.children&&e.children.length>0?a?(e.children=g(e.children,t,a),r.push({...e,title:m(e.title,t)})):(e.children=g(e.children,t),e.children.length>0&&r.push({...e,title:m(e.title,t)})):a&&r.push({...e,title:m(e.title,t)})})),r},f=(0,n.useMemo)((()=>{if(a){if(l){const e=g(JSON.parse(JSON.stringify(h)),l);return e.length?e:(p([{title:l,value:l},...t]),[{title:l,value:l}])}return"string"===typeof r.value?[{title:r.value,value:r.value},...t]:h}return g(JSON.parse(JSON.stringify(h)),l)}),[l,h]);return(0,n.useEffect)((()=>{"number"===typeof r.value&&p(t)}),[r.value]),(0,n.useEffect)((()=>{if(l){const e=g(JSON.parse(JSON.stringify(t)),l),a=e=>{let t=[];return e.forEach((e=>{t.push(e.value),e.children&&(t=t.concat(a(e.children)))})),t},r=a(e);u(r)}else u([])}),[t,l]),(0,n.useEffect)((()=>{p(t)}),[t]),(0,i.tZ)(s.Z,o()({filterTreeNode:()=>!0,treeExpandedKeys:d,onChange:t=>{c(""),e&&(r.labelInValue?e({...t,label:"string"===typeof t.label?t.label:t.label.props["test-data"]}):e(t))},treeData:f,onTreeExpand:e=>u(e),onSearch:e=>c(e)},r))}},917656:(e,t,a)=>{"use strict";a.r(t),a.d(t,{default:()=>Ka});var r=a(667294),o=a(828216),n=a(237731),s=a(522102),i=a(455867),l=a(478161),c=a(838703),d=a(672570),u=a(23525),h=a(427600),p=a(998286),m=a(991914),g=a(643399);const f={form_data:{name:"form_data",parser:e=>{const t=JSON.parse(e);if(t.datasource){const[e,a]=t.datasource.split("__");t.datasource_id=e,t.datasource_type=a,delete t.datasource}return t}},slice_id:{name:"slice_id"},datasource_id:{name:"datasource_id"},datasource_type:{name:"datasource_type"},datasource:{name:"datasource",parser:e=>{const[t,a]=e.split("__");return{datasource_id:t,datasource_type:a}}},form_data_key:{name:"form_data_key"},permalink_key:{name:"permalink_key"},viz_type:{name:"viz_type"},dashboard_id:{name:"dashboard_id"}},v={p:"permalink_key",table:"datasource_id"},b=e=>{const t=new URLSearchParams(e);return Array.from(t.keys()).reduce(((e,a)=>{var r;const o=t.get(a);if(null===o)return e;let n;try{var s,i,l;n=null!=(s=null==(i=(l=f[a]).parser)?void 0:i.call(l,o))?s:o}catch{n=o}if("object"===typeof n)return{...e,...n};const c=(null==(r=f[a])?void 0:r.name)||a;return{...e,[c]:n}}),{})},y=(e=window.location)=>{return new URLSearchParams(Object.entries({...b(e.search),...(t=e.pathname,Object.keys(v).reduce(((e,a)=>{const r=new RegExp(`/(${a})/(\\w+)`),o=t.match(r);return null!=o&&o[2]?{...e,[v[a]]:o[2]}:e}),{}))}).map((e=>e.join("="))).join("&"));var t};var S=a(476445),_=a(205872),w=a.n(_),Z=a(478718),x=a.n(Z),k=a(23279),T=a.n(k),C=a(45697),D=a.n(C),E=a(14890),N=a(751995),O=a(211965),I=a(68492),A=a(929119),$=a(667496),R=a(428615),M=a(514278),j=a(358593),U=a(741427),L=a(833626),z=a(731293),q=a(961337),P=a(599543),F=a(797381),Q=a(203741),K=a(294184),V=a.n(K),B=a(935500),H=a(550810),W=a(602275),J=a(301510),Y=a(340219),G=a(199068),X=a(112515),ee=a(410331),te=a(200651),ae=a(419485),re=a(174599),oe=a(906954),ne=a(414114),se=a(240323),ie=a(311064),le=a(46078),ce=a(355786),de=a(431069),ue=a(899612),he=a(132657),pe=a(591877),me=a(593185),ge=a(229487),fe=a(941331),ve=a(479217),be=a(95345),ye=a(989555),Se=a(737921),_e=a(730381),we=a.n(_e);const Ze=({cachedTimestamp:e})=>{const t=e?(0,O.tZ)("span",null,(0,i.t)("Loaded data cached"),(0,O.tZ)("b",null," ",we().utc(e).fromNow())):(0,i.t)("Loaded from cache");return(0,O.tZ)("span",{"data-test":"tooltip-content"},t,". ",(0,i.t)("Click to force-refresh"))},xe=({className:e,onClick:t,cachedTimestamp:a})=>{const[o,n]=(0,r.useState)(!1),s=o?"primary":"default";return(0,O.tZ)(j.u,{title:(0,O.tZ)(Ze,{cachedTimestamp:a}),id:"cache-desc-tooltip"},(0,O.tZ)(Se.Z,{className:`${e}`,type:s,onClick:t,onMouseOver:()=>n(!0),onMouseOut:()=>n(!1)},(0,i.t)("Cached")," ",(0,O.tZ)("i",{className:"fa fa-refresh"})))};var ke=a(444814);const Te=(0,N.iK)(Se.Z)`
  text-align: left;
  font-family: ${({theme:e})=>e.typography.families.monospace};
`;function Ce({endTime:e,isRunning:t,startTime:a,status:o="success"}){const[n,s]=(0,r.useState)("00:00:00.00"),i=(0,r.useRef)();return(0,r.useEffect)((()=>{const r=()=>{i.current&&(clearInterval(i.current),i.current=void 0)};return t&&(i.current=setInterval((()=>{if(a){const o=e||(0,ke.zO)();a<o&&s((0,ke.zQ)(a,o)),t||r()}}),30)),r}),[e,t,a]),(0,O.tZ)(Te,{type:o,role:"timer"},n)}var De;!function(e){e.failed="danger",e.loading="warning",e.success="success"}(De||(De={}));const Ee=(0,r.forwardRef)((({queriesResponse:e,chartStatus:t,chartUpdateStartTime:a,chartUpdateEndTime:r,refreshCachedQuery:o,rowLimit:n},s)=>{const i="loading"===t,l=null==e?void 0:e[0];return(0,O.tZ)("div",{ref:s},(0,O.tZ)("div",{css:e=>O.iv`
            display: flex;
            justify-content: flex-end;
            padding-bottom: ${4*e.gridUnit}px;
            & .ant-tag:last-of-type {
              margin: 0;
            }
          `},!i&&l&&(0,O.tZ)(ye.Z,{rowcount:Number(l.rowcount)||0,limit:Number(n)||0}),!i&&(null==l?void 0:l.is_cached)&&(0,O.tZ)(xe,{onClick:o,cachedTimestamp:l.cached_dttm}),(0,O.tZ)(Ce,{startTime:a,endTime:r,isRunning:i,status:De[t]})))}));var Ne=a(835932);const Oe=N.iK.div`
  ${({theme:e})=>O.iv`
    margin: ${4*e.gridUnit}px;
    padding: ${4*e.gridUnit}px;

    border: 1px solid ${e.colors.info.base};
    background-color: ${e.colors.info.light2};
    border-radius: 2px;

    color: ${e.colors.info.dark2};
    font-size: ${e.typography.sizes.m}px;

    p {
      margin-bottom: ${e.gridUnit}px;
    }

    & a,
    & span[role='button'] {
      color: inherit;
      text-decoration: underline;
      &:hover {
        color: ${e.colors.info.dark1};
      }
    }

    &.alert-type-warning {
      border-color: ${e.colors.alert.base};
      background-color: ${e.colors.alert.light2};

      p {
        color: ${e.colors.alert.dark2};
      }

      & a:hover,
      & span[role='button']:hover {
        color: ${e.colors.alert.dark1};
      }
    }
  `}
`,Ie=N.iK.div`
  display: flex;
  justify-content: flex-end;
  button {
    line-height: 1;
  }
`,Ae=N.iK.p`
  font-weight: ${({theme:e})=>e.typography.weights.bold};
`,$e={warning:"warning",danger:"danger"},Re=(0,r.forwardRef)((({title:e,bodyText:t,primaryButtonAction:a,secondaryButtonAction:r,primaryButtonText:o,secondaryButtonText:n,type:s="info",className:i=""},l)=>(0,O.tZ)(Oe,{className:`alert-type-${s} ${i}`,ref:l},(0,O.tZ)(Ae,null,e),(0,O.tZ)("p",null,t),o&&a&&(0,O.tZ)(Ie,null,r&&n&&(0,O.tZ)(Ne.Z,{buttonStyle:"link",buttonSize:"small",onClick:r},n),(0,O.tZ)(Ne.Z,{buttonStyle:s in $e?$e[s]:"primary",buttonSize:"small",onClick:a},o)))));var Me=a(775701);const je={actions:D().object.isRequired,onQuery:D().func,can_overwrite:D().bool.isRequired,can_download:D().bool.isRequired,datasource:D().object,dashboardId:D().number,column_formats:D().object,containerId:D().string.isRequired,isStarred:D().bool.isRequired,slice:D().object,sliceName:D().string,table_name:D().string,vizType:D().string.isRequired,form_data:D().object,ownState:D().object,standalone:D().bool,force:D().bool,timeout:D().number,chartIsStale:D().bool,chart:W.$6,errorMessage:D().node,triggerRender:D().bool},Ue=1.25,Le=[100,0],ze=[150,65],qe=N.iK.div`
  display: flex;
  flex-direction: column;
  align-items: stretch;
  align-content: stretch;
  overflow: auto;
  box-shadow: none;
  height: 100%;

  & > div {
    height: 100%;
  }

  .gutter {
    border-top: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
    border-bottom: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
    width: ${({theme:e})=>9*e.gridUnit}px;
    margin: ${({theme:e})=>e.gridUnit*Ue}px auto;
  }

  .gutter.gutter-vertical {
    display: ${({showSplite:e})=>e?"block":"none"};
    cursor: row-resize;
    position: relative;
    z-index: 11;
  }

  .ant-collapse {
    .ant-tabs {
      height: 100%;
      .ant-tabs-nav {
        padding-left: ${({theme:e})=>5*e.gridUnit}px;
        margin: 0;
      }
      .ant-tabs-content-holder {
        overflow: hidden;
        .ant-tabs-content {
          height: 100%;
        }
      }
    }
  }
`;var Pe={name:"1wbll7q",styles:"text-decoration:underline"};const Fe=({chart:e,slice:t,vizType:a,ownState:o,triggerRender:n,force:s,datasource:l,errorMessage:c,form_data:d,onQuery:u,actions:h,timeout:p,standalone:m,chartIsStale:g,chartAlert:f})=>{var v;const b=(0,N.Fg)(),y=b.gridUnit*Ue,S=b.gridUnit*Ue,{width:_,height:w,ref:Z}=(0,ue.NB)({refreshMode:"debounce",refreshRate:300}),[x,k]=(0,r.useState)((0,pe.cr)(me.T.DATAPANEL_CLOSED_BY_DEFAULT)?Le:(0,q.rV)(q.dR.chart_split_sizes,Le)),[T,C]=(0,r.useState)(!(0,pe.cr)(me.T.DATAPANEL_CLOSED_BY_DEFAULT)&&(0,q.rV)(q.dR.is_datapanel_open,!1)),[D,E]=(0,r.useState)(!1),I=(0,ie.Z)(),{useLegacyApi:A}=null!=(v=I.get(a))?v:{},$=A&&l.type!==le.i9.Table,R=!f&&g&&!$&&"failed"!==e.chartStatus&&(0,ce.Z)(e.queriesResponse).length>0,M=(0,r.useCallback)((async function(){if(t&&null===t.query_context){const e=(0,X.u)({formData:t.form_data,force:s,resultFormat:"json",resultType:"full",setDataMask:null,ownState:null});await de.Z.put({endpoint:`/api/v1/chart/${t.slice_id}`,headers:{"Content-Type":"application/json"},body:JSON.stringify({query_context:JSON.stringify(e),query_context_generation:!0})})}}),[t]);(0,r.useEffect)((()=>{M()}),[M]),(0,r.useEffect)((()=>{(0,q.LS)(q.dR.chart_split_sizes,x)}),[x]);const j=(0,r.useCallback)((e=>{k(e)}),[]),U=(0,r.useCallback)((()=>{h.setForceQuery(!0),h.postChartFormData(d,!0,p,e.id,void 0,o),h.updateQueryFormData(d,e.id)}),[h,e.id,d,o,p]),L=(0,r.useCallback)((e=>{let t;t=e?[60,40]:Le,k(t),C(e)}),[]),z=(0,r.useCallback)((()=>(0,O.tZ)("div",{css:O.iv`
          min-height: 0;
          flex: 1;
          overflow: hidden;
        `,ref:Z},_&&w&&(0,O.tZ)(he.Z,{width:Math.floor(_),height:w,ownState:o,annotationData:e.annotationData,chartAlert:e.chartAlert,chartStackTrace:e.chartStackTrace,chartId:e.id,chartStatus:e.chartStatus,triggerRender:n,force:s,datasource:l,errorMessage:c,formData:d,latestQueryFormData:e.latestQueryFormData,onQuery:u,queriesResponse:e.queriesResponse,chartIsStale:g,setControlValue:h.setControlValue,timeout:p,triggerQuery:e.triggerQuery,vizType:a}))),[h.setControlValue,e.annotationData,e.chartAlert,e.chartStackTrace,e.chartStatus,e.id,e.latestQueryFormData,e.queriesResponse,e.triggerQuery,g,w,Z,_,l,c,s,d,u,o,p,n,a]),P=(0,r.useMemo)((()=>(0,O.tZ)("div",{className:"panel-body",css:O.iv`
          display: flex;
          flex-direction: column;
        `},$&&(0,O.tZ)(ge.Z,{message:(0,i.t)("Chart type requires a dataset"),type:"error",css:e=>O.iv`
              margin: 0 0 ${4*e.gridUnit}px 0;
            `,description:(0,O.tZ)(r.Fragment,null,(0,i.t)("This chart type is not supported when using an unsaved query as a chart source. "),(0,O.tZ)("span",{role:"button",tabIndex:0,onClick:()=>E(!0),css:Pe},(0,i.t)("Create a dataset")),(0,i.t)(" to visualize your data."))}),R&&(0,O.tZ)(Re,{title:c?(0,i.t)("Required control values have been removed"):(0,i.t)("Your chart is not up to date"),bodyText:c?(0,Me.J)(!1):(0,O.tZ)("span",null,(0,i.t)('You updated the values in the control panel, but the chart was not updated automatically. Run the query by clicking on the "Update chart" button or')," ",(0,O.tZ)("span",{role:"button",tabIndex:0,onClick:u},(0,i.t)("click here")),"."),type:"warning",css:e=>O.iv`
              margin: 0 0 ${4*e.gridUnit}px 0;
            `}),(0,O.tZ)(Ee,{queriesResponse:e.queriesResponse,chartStatus:e.chartStatus,chartUpdateStartTime:e.chartUpdateStartTime,chartUpdateEndTime:e.chartUpdateEndTime,refreshCachedQuery:U,rowLimit:null==d?void 0:d.row_limit}),z())),[R,c,u,e.queriesResponse,e.chartStatus,e.chartUpdateStartTime,e.chartUpdateEndTime,U,null==d?void 0:d.row_limit,z]),F=(0,r.useMemo)((()=>z()),[z]),[Q,K]=(0,r.useState)(e.latestQueryFormData);(0,r.useEffect)((()=>{n||K(e.latestQueryFormData)}),[e.latestQueryFormData]);const V=(0,r.useCallback)(((e,t,a)=>({[e]:`calc(${t}% - ${a+y}px)`})),[y]);if(m){const e="background-transparent";return document.body.className.split(" ").includes(e)||(document.body.className+=` ${e}`),F}return(0,O.tZ)(qe,{className:"panel panel-default chart-container",showSplite:T},"filter_box"===a?P:(0,O.tZ)(se.Z,{sizes:x,minSize:ze,direction:"vertical",gutterSize:S,onDragEnd:j,elementStyle:V,expandToMin:!0},P,(0,O.tZ)(be.c9,{ownState:o,queryFormData:Q,datasource:l,queryForce:s,onCollapseChange:L,chartStatus:e.chartStatus,errorMessage:c,actions:h})),D&&(0,O.tZ)(fe.W,{visible:D,onHide:()=>E(!1),buttonTextOnSave:(0,i.t)("Save"),buttonTextOnOverwrite:(0,i.t)("Overwrite"),datasource:(0,ve.z)(l),openWindow:!1,formData:d}))};Fe.propTypes=je;const Qe=Fe;var Ke=a(121804),Ve=a.n(Ke),Be=a(5364),He=a(958452),We=a(837687),Je=a(748989),Ye=a(945211),Ge=a(349484),Xe=a(948205),et=a(855241),tt=a(71577),at=a(843700),rt=a(171262),ot=a(774069);function nt({controls:e,controlColSize:t}){const a=(0,r.useCallback)((e=>{var t,a;return"HiddenControl"===(null==e||null==(t=e.props)?void 0:t.type)||!1===(null==e||null==(a=e.props)?void 0:a.isVisible)}),[]),o=e.filter((e=>!a(e))),n=t||(o.length?12/o.length:12);return(0,O.tZ)("div",{className:"row"},e.map(((e,t)=>(0,O.tZ)("div",{className:`col-lg-${n} col-xs-12`,style:{display:a(e)?"none":"block"},key:t},e))))}var st=a(615542);const it=({loading:e,onQuery:t,onStop:a,errorMessage:r,isNewChart:o,canStopQuery:n,chartIsStale:s})=>e?(0,O.tZ)(Ne.Z,{onClick:a,buttonStyle:"warning",disabled:!n},(0,O.tZ)("i",{className:"fa fa-stop-circle-o"})," ",(0,i.t)("Stop")):(0,O.tZ)(Ne.Z,{onClick:t,buttonStyle:s?"primary":"secondary",disabled:!!r,"data-test":"run-query-button"},o?(0,i.t)("Create chart"):(0,i.t)("Update chart"));var lt=a(269856);const{confirm:ct}=ot.Z,dt=O.iv`
  &.anticon {
    font-size: unset;
    .anticon {
      line-height: unset;
      vertical-align: unset;
    }
  }
`,ut=e=>O.iv`
  display: flex;
  position: sticky;
  bottom: 0;
  flex-direction: column;
  align-items: center;
  padding: ${4*e.gridUnit}px;
  z-index: 999;
  background: linear-gradient(
    ${(0,Ge.rgba)(e.colors.grayscale.light5,0)},
    ${e.colors.grayscale.light5} ${e.opacity.mediumLight}
  );

  & > button {
    min-width: 156px;
  }
`,ht=N.iK.div`
  position: relative;
  height: 100%;
  width: 100%;

  // Resizable add overflow-y: auto as a style to this div
  // To override it, we need to use !important
  overflow: visible !important;
  #controlSections {
    height: 100%;
    overflow: visible;
  }
  .nav-tabs {
    flex: 0 0 1;
  }
  .tab-content {
    overflow: auto;
    flex: 1 1 100%;
  }
  .Select__menu {
    max-width: 100%;
  }
  .type-label {
    margin-right: ${({theme:e})=>3*e.gridUnit}px;
    width: ${({theme:e})=>7*e.gridUnit}px;
    display: inline-block;
    text-align: center;
    font-weight: ${({theme:e})=>e.typography.weights.bold};
  }
`,pt=(0,N.iK)(rt.ZP)`
  ${({theme:e,fullWidth:t})=>O.iv`
    height: 100%;
    overflow: visible;
    .ant-tabs-nav {
      margin-bottom: 0;
    }
    .ant-tabs-nav-list {
      width: ${t?"100%":"50%"};
    }
    .ant-tabs-tabpane {
      height: 100%;
    }
    .ant-tabs-content-holder {
      padding-top: ${4*e.gridUnit}px;
    }

    .ant-collapse-ghost > .ant-collapse-item {
      &:not(:last-child) {
        border-bottom: 1px solid ${e.colors.grayscale.light3};
      }

      & > .ant-collapse-header {
        font-size: ${e.typography.sizes.s}px;
        background-color: ${e.colors.grayscale.light4};
      }

      & > .ant-collapse-content > .ant-collapse-content-box {
        padding-bottom: 0;
        font-size: ${e.typography.sizes.s}px;
      }
    }
  `}
`,mt=(e,t)=>e.reduce(((e,a)=>!a.expanded&&a.label||(e=>!!e.label&&(Je.sections.legacyRegularTime.label===e.label||Je.sections.legacyTimeseriesTime.label===e.label))(a)&&!(e=>{var t;return null==e||null==(t=e.columns)?void 0:t.some((e=>e.is_dttm))})(t)?e:[...e,String(a.label)]),[]);function gt(e,t){const a=(0,r.useRef)(e()),o=(0,r.useRef)(t);return o.current!==t&&(a.current=e(),o.current=t),a}const ft=e=>{var t,a;const{colors:s}=(0,N.Fg)(),l=(0,r.useContext)(M.Zn),d=(0,U.D)(e.exploreState),u=(0,U.D)(e.exploreState.datasource),h=(0,U.D)(e.chart.chartStatus),[p,m]=(0,r.useState)(!1),g=(0,r.useRef)(null),f=(0,o.v9)((e=>e.explore.controlsTransferred)),v=(0,o.v9)((e=>{var t,a;return null==(t=e.common)||null==(a=t.conf)?void 0:a.DEFAULT_TIME_FILTER})),{form_data:b,actions:y}=e,{setControlValue:S}=y,{x_axis:_,adhoc_filters:Z}=b,x=(0,U.D)(_),[k,T]=(0,r.useState)("main");(0,r.useEffect)((()=>{if(_&&_!==x&&(0,Ye.x)(_,e.exploreState.datasource)){(!Z||!Z.find((e=>"SIMPLE"===e.expressionType&&e.operator===lt.d.TEMPORAL_RANGE&&e.subject===_)))&&ct({title:(0,i.t)("The X-axis is not on the filters list"),content:(0,i.t)("The X-axis is not on the filters list which will prevent it from being used in\n            time range filters in dashboards. Would you like to add it to the filters list?"),onOk:()=>{S("adhoc_filters",[...Z||[],{clause:"WHERE",subject:_,operator:lt.d.TEMPORAL_RANGE,comparator:v||Be.vM,expressionType:"SIMPLE"}])}})}}),[_,Z,S,v,x,e.exploreState.datasource]),(0,r.useEffect)((()=>{let t=!1;const a=e=>"object"===typeof e&&(0,n.Z)(e)&&"datasourceWarning"in e&&!0===e.datasourceWarning?(t=!0,{...e,datasourceWarning:!1}):e;"success"===e.chart.chartStatus&&"success"!==h&&(null==f||f.forEach((r=>{var o;if(t=!1,!(0,n.Z)(e.controls[r]))return;const s=Array.isArray(e.controls[r].value)?null==(o=(0,ce.Z)(e.controls[r].value))?void 0:o.map(a):a(e.controls[r].value);t&&e.actions.setControlValue(r,s)})))}),[f,h,e.actions,e.chart.chartStatus,e.controls]),(0,r.useEffect)((()=>{var t,a,r;!u||u.type===le.i9.Query||(null==(t=e.exploreState.datasource)?void 0:t.id)===u.id&&(null==(a=e.exploreState.datasource)?void 0:a.type)===u.type||(m(!0),null==(r=g.current)||r.scrollTo(0,0))}),[null==(t=e.exploreState.datasource)?void 0:t.id,null==(a=e.exploreState.datasource)?void 0:a.type,u]);const{expandedQuerySections:C,expandedCustomizeSections:D,querySections:E,customizeSections:I}=(0,r.useMemo)((()=>function(e,t,a){const r=[],o=[];return(0,ee.Bq)(e,a).forEach((e=>{"data"===e.tabOverride||e.controlSetRows.some((e=>e.some((e=>e&&"object"===typeof e&&"config"in e&&e.config&&(!e.config.renderTrigger||"data"===e.config.tabOverride)))))?r.push(e):e.controlSetRows.length>0&&o.push(e)})),{expandedQuerySections:mt(r,t),expandedCustomizeSections:mt(o,t),querySections:r,customizeSections:o}}(b.viz_type,e.exploreState.datasource,e.datasource_type)),[e.exploreState.datasource,b.viz_type,e.datasource_type]),A=(0,r.useCallback)((()=>{(0,ce.Z)(e.exploreState.controlsTransferred).forEach((t=>e.actions.setControlValue(t,e.controls[t].default)))}),[e.actions,e.exploreState.controlsTransferred,e.controls]),$=(0,r.useCallback)((()=>{A(),m(!1)}),[A]),R=(0,r.useCallback)((()=>{m(!1)}),[]),L=({name:t,config:a})=>{const{controls:r,chart:o,exploreState:n}=e;return Boolean(null==a.shouldMapStateToProps?void 0:a.shouldMapStateToProps(d||n,n,r[t],o))},q=({name:t,config:a})=>{const{controls:r,chart:o,exploreState:n}=e,{visibility:s}=a,l={...a,...r[t],...L({name:t,config:a})?null==a||null==a.mapStateToProps?void 0:a.mapStateToProps(n,r[t],o):void 0,name:t},{validationErrors:c,label:d,description:u,...h}=l,p=s?s.call(a,e,l):void 0,m="function"===typeof d?d(n,r[t],o):d,g="function"===typeof u?u(n,r[t],o):u;return"adhoc_filters"===t&&(h.canDelete=(e,t)=>{const a=e=>e.operator===lt.d.TEMPORAL_RANGE;if(a(e)){if(1===t.filter(a).length)return(0,i.t)("You cannot delete the last temporal filter as it's used for time range filters in dashboards.")}return!0}),(0,O.tZ)(st.Z,w()({key:`control-${t}`,name:t,label:m,description:g,validationErrors:c,actions:e.actions,isVisible:p},h))},P=gt((()=>({})),b.viz_type),F=t=>{const{controls:a}=e,{label:o,description:n}=t,l=String(o),c=t.controlSetRows.some((e=>e.some((e=>{const t="string"===typeof e?e:e&&"name"in e?e.name:null;return t&&t in a&&a[t].validationErrors&&a[t].validationErrors.length>0}))));c||(P.current[l]=!0);const d=P.current[l]?s.error.base:s.alert.base,u=()=>(0,O.tZ)("span",{"data-test":"collapsible-control-panel-header"},(0,O.tZ)("span",{css:e=>O.iv`
            font-size: ${e.typography.sizes.m}px;
            line-height: 1.3;
          `},o)," ",n&&(0,O.tZ)(j.u,{id:l,title:n},(0,O.tZ)(z.Z.InfoCircleOutlined,{css:dt})),c&&(0,O.tZ)(j.u,{id:`${Ve()("validation-errors")}-tooltip`,title:(0,i.t)("This section contains validation errors")},(0,O.tZ)(z.Z.InfoCircleOutlined,{css:O.iv`
                ${dt};
                color: ${d};
              `}))),h=e=>O.iv`
      margin-bottom: 0;
      box-shadow: none;
      &:last-child {
        padding-bottom: ${16*e.gridUnit}px;
        border-bottom: 0;
      }
      .panel-body {
        margin-left: ${4*e.gridUnit}px;
        padding-bottom: 0;
      }
      span.label {
        display: inline-block;
      }
      ${!t.label&&"\n        .ant-collapse-header {\n          display: none;\n        }\n      "}
    `,p=e=>T(e),m=(e=>{const t=[];for(let r=0;r<e.length;r++){const o=e[r];for(let e=0;e<o.length;e++){var a;const r=o[e];(null==r||null==(a=r.name)||null==a.indexOf?void 0:a.indexOf("_inst_"))>=0&&t.push(r)}}return t})(t.controlSetRows);if(m.length){const e=(e=>{const t=[],a=[],r=[];for(let o=0;o<e.length;o++){const n=e[o];n.name.indexOf("main_")>=0&&t.push(n),n.name.indexOf("secondary_")>=0&&a.push(n),(n.name.indexOf("end_")>=0||n.name.indexOf("thirdary_")>=0)&&r.push(n)}return[{label:(0,i.t)("Main indicators"),value:"main",data:t},{label:(0,i.t)("Secondary indicators"),value:"secondary",data:a},{label:(0,i.t)("End indicator"),value:"end",data:r}]})(m),t=(0,O.tZ)(Xe.Z,{defaultActiveKey:k,onChange:p},e.map((e=>{const t=e.data.map((e=>e?r.isValidElement(e)?e:e.name&&e.config&&"datasource"!==e.name?q(e):null:null)).filter((e=>null!==e));return(0,O.tZ)(Xe.Z.TabPane,{tab:e.label,key:e.value},t)})));return(0,O.tZ)(at.Z.Panel,{css:h,header:(0,O.tZ)(u,null),key:l},(0,O.tZ)(et.Z,{trigger:["click"],content:t,title:(0,i.t)("Set indicator properties")},(0,O.tZ)(tt.Z,{type:"dashed",icon:(0,O.tZ)(He.default,null),style:{width:"100%"}},(0,i.t)("Set indicator properties"))))}return(0,O.tZ)(at.Z.Panel,{css:h,header:(0,O.tZ)(u,null),key:l},t.controlSetRows.map(((e,t)=>{const a=e.map((e=>e?r.isValidElement(e)?e:e.name&&e.config&&"datasource"!==e.name?q(e):null:null)).filter((e=>null!==e));return 0===a.length?null:(0,O.tZ)(nt,{key:`controlsetrow-${t}`,controls:a})})))},Q=(0,ce.Z)(e.exploreState.controlsTransferred).length>0,K=(0,r.useCallback)((()=>Q?(0,O.tZ)(Re,{title:(0,i.t)("Keep control settings?"),bodyText:(0,i.t)("You've changed datasets. Any controls with data (columns, metrics) that match this new dataset have been retained."),primaryButtonAction:R,secondaryButtonAction:$,primaryButtonText:(0,i.t)("Continue"),secondaryButtonText:(0,i.t)("Clear form"),type:"info"}):(0,O.tZ)(Re,{title:(0,i.t)("No form settings were maintained"),bodyText:(0,i.t)("We were unable to carry over any controls when switching to this new dataset."),primaryButtonAction:R,primaryButtonText:(0,i.t)("Continue"),type:"warning"})),[$,R,Q]),V=gt((()=>!1),b.viz_type),B=(0,r.useMemo)((()=>{e.errorMessage||(V.current=!0);const t=V.current?s.error.base:s.alert.base;return(0,O.tZ)(r.Fragment,null,(0,O.tZ)("span",null,(0,i.t)("Data")),e.errorMessage&&(0,O.tZ)("span",{css:e=>O.iv`
              margin-left: ${2*e.gridUnit}px;
            `}," ",(0,O.tZ)(j.u,{id:"query-error-tooltip",placement:"right",title:e.errorMessage},(0,O.tZ)(z.Z.ExclamationCircleOutlined,{css:O.iv`
                  ${dt};
                  color: ${t};
                `}))))}),[s.error.base,s.alert.base,V,e.errorMessage]);if(!(0,We.Z)().has(b.viz_type)&&l.loading)return(0,O.tZ)(c.Z,null);const H=I.length>0;return(0,O.tZ)(ht,{ref:g},(0,O.tZ)(pt,{id:"controlSections","data-test":"control-tabs",fullWidth:H,allowOverflow:!1,animated:!0},(0,O.tZ)(rt.ZP.TabPane,{key:"query",tab:B},(0,O.tZ)(at.Z,{defaultActiveKey:C,expandIconPosition:"right",ghost:!0},p&&(0,O.tZ)(K,null),E.map(F))),H&&(0,O.tZ)(rt.ZP.TabPane,{key:"display",tab:(0,i.t)("Customize")},(0,O.tZ)(at.Z,{defaultActiveKey:D,expandIconPosition:"right",ghost:!0},I.map(F)))),(0,O.tZ)("div",{css:ut},(0,O.tZ)(it,{onQuery:e.onQuery,onStop:e.onStop,errorMessage:e.errorMessage,loading:"loading"===e.chart.chartStatus,isNewChart:!e.chart.queriesResponse,canStopQuery:e.canStopQuery,chartIsStale:e.chartIsStale})))};var vt=a(616550),bt=a(409882),yt=a(454076),St=a(9875),_t=a(49238),wt=a(287183),Zt=a(970553),xt=a(748086),kt=a(888154);const Tt="save_chart_recent_dashboard",Ct=(0,N.iK)(ot.Z)`
  .ant-modal-body {
    overflow: visible;
  }
  i {
    position: absolute;
    top: -${({theme:e})=>5.25*e.gridUnit}px;
    left: ${({theme:e})=>26.75*e.gridUnit}px;
  }
`;class Dt extends r.Component{constructor(e){var t;super(e),this.handleDatasetNameChange=e=>{this.setState({datasetName:e.target.value})},this.renderSaveChartModal=()=>{var e;let{TreeMenus:t,checkedKeys:a,isDashboard:r,checkedKeysdash:o,TreeMenusdash:n,dashboardTreeOptions:s}=this.state;const l=this.state.saveToDashboardId||this.state.newDashboardName;return(0,O.tZ)(_t.l0,{"data-test":"save-modal-body",layout:"vertical"},(this.state.alert||this.props.alert)&&(0,O.tZ)(ge.Z,{type:"warning",message:this.state.alert||this.props.alert,onClose:this.removeAlert}),(0,O.tZ)(_t.xJ,{"data-test":"radio-group"},(0,O.tZ)(wt.Y,{id:"overwrite-radio",disabled:!this.canOverwriteSlice(),checked:"overwrite"===this.state.action,onChange:()=>this.changeAction("overwrite"),"data-test":"save-overwrite-radio"},(0,i.t)("Save (Overwrite)")),(0,O.tZ)(wt.Y,{id:"saveas-radio","data-test":"saveas-radio",checked:"saveas"===this.state.action,onChange:()=>this.changeAction("saveas")},(0,i.t)("Save as..."))),(0,O.tZ)("hr",null),(0,O.tZ)(_t.xJ,{label:(0,i.t)("Chart name"),required:!0},(0,O.tZ)(St.II,{name:"new_slice_name",type:"text",placeholder:"Name",value:this.state.newSliceName,onChange:this.onSliceNameChange,"data-test":"new-chart-name"})),(0,O.tZ)(_t.xJ,{label:(0,i.t)("Select Chart Group"),required:!0},(0,O.tZ)(Zt.Z,{labelInValue:!0,showSearch:!0,value:a,dropdownStyle:{maxHeight:400,overflow:"auto"},placeholder:(0,i.t)("Please select"),onChange:this.onSelect,treeData:t,treeNodeFilterProp:"title"})),"query"===(null==(e=this.props.datasource)?void 0:e.type)&&(0,O.tZ)(_t.xJ,{label:(0,i.t)("Dataset Name"),required:!0},(0,O.tZ)(bt.V,{tooltip:(0,i.t)("A reusable dataset will be saved with your chart."),placement:"right"}),(0,O.tZ)(St.II,{name:"dataset_name",type:"text",placeholder:"Dataset Name",value:this.state.datasetName,onChange:this.handleDatasetNameChange,"data-test":"new-dataset-name"})),(0,O.tZ)(_t.xJ,{label:(0,i.t)("Add to dashboard"),"data-test":"save-chart-modal-select-dashboard-form"},(0,O.tZ)(kt.Z,{allowClear:!0,showSearch:!0,allowNewOptions:!0,treeData:s,onChange:this.onDashboardSelectChange,value:l||void 0,placeholder:(0,O.tZ)("div",null,(0,O.tZ)("b",null,(0,i.t)("Select")),(0,i.t)(" a dashboard OR "),(0,O.tZ)("b",null,(0,i.t)("create")),(0,i.t)(" a new one"))})),r&&(0,O.tZ)(_t.xJ,{label:(0,i.t)("Select Dashboard Group"),required:!0},(0,O.tZ)(Zt.Z,{labelInValue:!0,showSearch:!0,value:o,dropdownStyle:{maxHeight:400,overflow:"auto"},placeholder:(0,i.t)("Please select"),onChange:this.onSelectdash,treeData:n,treeNodeFilterProp:"title"})))},this.renderFooter=()=>{var e,t;const a=(0,yt.w)();return(0,O.tZ)("div",{"data-test":"save-modal-footer"},(0,O.tZ)(Ne.Z,{id:"btn_cancel",buttonSize:"small",onClick:this.onHide},(0,i.t)("Cancel")),!a&&(0,O.tZ)(Ne.Z,{id:"btn_modal_save_goto_dash",buttonSize:"small",disabled:!this.state.newSliceName||!this.state.saveToDashboardId&&!this.state.newDashboardName||(null==(e=this.props.datasource)?void 0:e.type)!==le.i9.Table&&!this.state.datasetName,onClick:()=>this.saveOrOverwrite(!0)},this.isNewDashboard()?(0,i.t)("Save & go to new dashboard"):(0,i.t)("Save & go to dashboard")),(0,O.tZ)(Ne.Z,{id:"btn_modal_save",buttonSize:"small",buttonStyle:"primary",onClick:()=>this.saveOrOverwrite(!1),disabled:this.state.isLoading||!this.state.newSliceName||(null==(t=this.props.datasource)?void 0:t.type)!==le.i9.Table&&!this.state.datasetName,"data-test":"btn-modal-save"},!this.canOverwriteSlice()&&this.props.slice?(0,i.t)("Save as new chart"):this.isNewDashboard()?(0,i.t)("Save to new dashboard"):(0,i.t)("Save")))},this.state={saveToDashboardId:null,newSliceName:e.sliceName,datasetName:null==(t=e.datasource)?void 0:t.name,alert:null,action:this.canOverwriteSlice()?"overwrite":"saveas",isLoading:!1,TreeMenus:[],expandedKeys:[],group_id:"",dashboarddata:[],isDashboard:!1,checkedKeysdash:null,TreeMenusdash:[],dashboardTreeOptions:[],dashgroup_id:"",checkedKeys:null,chartPid:sessionStorage.getItem("chartGroup_id")},this.onDashboardSelectChange=this.onDashboardSelectChange.bind(this),this.onSliceNameChange=this.onSliceNameChange.bind(this),this.changeAction=this.changeAction.bind(this),this.saveOrOverwrite=this.saveOrOverwrite.bind(this),this.isNewDashboard=this.isNewDashboard.bind(this),this.removeAlert=this.removeAlert.bind(this),this.onHide=this.onHide.bind(this),this.onSelect=this.onSelect.bind(this),this.onSelectdash=this.onSelectdash.bind(this)}isNewDashboard(){return!(this.state.saveToDashboardId||!this.state.newDashboardName)}canOverwriteSlice(){return window.location.href.indexOf("slice_id")>-1}componentDidMount(){this.props.actions.fetchDashboards(this.props.userId).then((()=>{var e;if(0===(0,ce.Z)(this.props.dashboards).length)return;const t=null==(e=this.props.dashboards)?void 0:e.map((e=>e.value)),a=sessionStorage.getItem(Tt);let r=a&&parseInt(a,10);this.props.dashboardId&&(r=this.props.dashboardId),null!==r&&-1!==t.indexOf(r)&&this.setState({saveToDashboardId:r})})),this.DealList(),this.DealdashboardList(),this.getDashboardList(),this.getdashboarddata("")}componentDidUpdate(e,t){this.state.action!==t.action&&this.DealList()}getdashboarddata(e){return de.Z.get({endpoint:`/api/v2/dashboard/?limt='10000'&title=${e}`}).then((e=>{if(200==e.json.meta.code||201==e.json.meta.code){let t=[];e.json.meta.data.map((e=>{t.push({label:e.dashboard_title,value:e.id})})),this.setState({dashboarddata:t})}else xt.ZP.error(e.json.meta.message)}))}DealList(){const{chartPid:e}=this.state;return de.Z.get({endpoint:"/api/v2/chart/group/"}).then((t=>{if(200==t.json.meta.code||201==t.json.meta.code){if(this.forEach_children(t.json.meta.data,""),this.setState({TreeMenus:t.json.meta.data}),e){let a=this.loopPname(t.json.meta.data,e);this.setState({checkedKeys:a,group_id:a.value})}}else xt.ZP.error(t.json.meta.message)}))}DealdashboardList(){return de.Z.get({endpoint:"/api/v2/dashboard/group/tree/"}).then((e=>{200==e.json.meta.code||201==e.json.meta.code?(e.json.meta.data.forEach((e=>{e.title=e.name,e.allname=e.name,e.value=e.group_id,e.children.length>0&&this.forEach_children(e.children,e.name)})),this.setState({TreeMenusdash:e.json.meta.data})):xt.ZP.error(e.json.meta.message)}))}getDashboardList(){return de.Z.get({endpoint:"/api/v2/dashboard/group/"}).then((e=>{if(200==e.json.meta.code||201==e.json.meta.code){const t=e.json.meta.data||[],a=e=>e&&e.length?e.map((e=>({title:e.name,value:e.group_id,selectable:!1,children:[...a(e.children),...e.dashboards.map((e=>({title:e.dashboard_title,value:e.dashboard_id})))]}))):[],r=a(t);this.setState({dashboardTreeOptions:r})}else xt.ZP.error(e.json.meta.message)}))}forEach_children(e,t){const{chartPid:a,action:r}=this.state;e.forEach((e=>{e.title=e.name,e.allname=t?`${t}-${e.name}`:e.name,e.value=e.group_id,e.disabled=("overwrite"!=r||e.group_id!=a)&&e.perm<4,e.children.length>0&&this.forEach_children(e.children,e.name)}))}onSliceNameChange(e){this.setState({newSliceName:e.target.value})}onDashboardSelectChange(e){const t=e?String(e):void 0,a=e&&"number"===typeof e?e:null;a||!e?this.setState({isDashboard:!1}):this.setState({isDashboard:!0}),this.setState({saveToDashboardId:a,newDashboardName:t})}changeAction(e){this.setState({action:e,checkedKeys:null})}onHide(){this.props.dispatch((0,ae.setSaveChartModalVisibility)(!1))}async saveOrOverwrite(e){let{group_id:t,isDashboard:a,dashgroup_id:r}=this.state;if(""==t||null==t)return xt.ZP.error((0,i.t)("Please select Chart a group"));if(a&&null==r)return xt.ZP.error((0,i.t)("Please select dashboard a group"));let o=t,s=r;this.setState({alert:null,isLoading:!0}),this.props.actions.removeSaveModalAlert();try{var l;if((null==(l=this.props.datasource)?void 0:l.type)===le.i9.Query){var c;const{schema:e,sql:t,database:a}=this.props.datasource,{templateParams:r}=this.props.datasource,o=(null==(c=this.props.datasource)?void 0:c.columns)||[];await this.props.actions.saveDataset({schema:e,sql:t,database:a,templateParams:r,datasourceName:this.state.datasetName,columns:o})}let t=[];this.props.slice&&"overwrite"===this.state.action&&(t=await this.props.actions.getSliceDashboards(this.props.slice));const a=this.props.form_data||{};delete a.url_params;let r,i=null;if(this.state.newDashboardName||this.state.saveToDashboardId){var d;let e=this.state.saveToDashboardId||null;if(!this.state.saveToDashboardId){e=(await this.props.actions.createDashboard(this.state.newDashboardName,s)).id,this.setState({saveToDashboardId:e})}i=(await this.props.actions.getDashboard(e)).result,(0,n.Z)(i)&&(0,n.Z)(null==(d=i)?void 0:d.id)&&(t=t.includes(i.id)?t:[...t,i.id],a.dashboards=t)}if(this.props.actions.setFormData({...a}),"overwrite"===this.state.action){const e=this.props.slice||sessionStorage.getItem("chartIds");r=await this.props.actions.updateSlice(this.props.slice||{slice_id:e,owners:[10,2]},this.state.newSliceName,t,i?{title:i.dashboard_title,new:!this.state.saveToDashboardId}:null,o)}else{let e=[];r=await this.props.actions.createSlice(this.state.newSliceName,t,i?{title:i.dashboard_title,new:!this.state.saveToDashboardId}:null,e,o)}if(i?sessionStorage.setItem(Tt,`${i.id}`):sessionStorage.removeItem(Tt),o){if(e)return window.location.assign("/dashboard/list/"),void sessionStorage.setItem("daidOrSlug_ids",this.state.saveToDashboardId+"");{window.location.assign("/chart/list/"),sessionStorage.setItem("chartIds",r.id),sessionStorage.setItem("chartTitle",this.state.newSliceName);const e=[],t=a=>{if(a&&a.length)return a.some((a=>a.group_id===this.state.checkedKeys.value?(e.unshift(`${a.group_id}`),!0):a.children&&a.children.length?(e.unshift(`${a.group_id}`),t(a.children)):(e.shift(),!1)))};return sessionStorage.setItem("key",`${r.id}&&${this.state.newSliceName}`),t(this.state.TreeMenus),void sessionStorage.setItem("keyPath",JSON.stringify(e))}}if(e&&i)return void this.props.history.push(i.url);const u=new URLSearchParams(window.location.search);u.set("save_action",this.state.action),u.delete("form_data_key"),"saveas"===this.state.action&&u.set("slice_id",r.id.toString()),this.props.history.replace(`/explore/?${u.toString()}`),this.setState({isLoading:!1}),this.onHide()}finally{this.setState({isLoading:!1})}}loopPname(e,t){let a={},r=(e,o)=>{e.map((e=>{e.value==o&&(a={label:e.allname,value:e.value}),e.children.length>0&&r(e.children,t)}))};return r(e,t),a}onSelect(e){let{TreeMenus:t}=this.state,a=this.loopPname(t,e.value);this.setState({checkedKeys:a,group_id:a.value})}onSelectdash(e){let{TreeMenusdash:t}=this.state,a=this.loopPname(t,e.value);this.setState({checkedKeysdash:a,dashgroup_id:a.value})}removeAlert(){this.props.alert&&this.props.actions.removeSaveModalAlert(),this.setState({alert:null})}render(){return(0,O.tZ)(Ct,{show:this.props.isVisible,onHide:this.onHide,title:(0,i.t)("Save chart"),footer:this.renderFooter()},this.state.isLoading?(0,O.tZ)("div",{css:O.iv`
              display: flex;
              justify-content: center;
            `},(0,O.tZ)(c.Z,{position:"normal"})):this.renderSaveChartModal())}}const Et=(0,vt.EN)((0,o.$j)((function({explore:e,saveModal:t,user:a}){return{datasource:e.datasource,slice:e.slice,userId:null==a?void 0:a.userId,dashboards:t.dashboards,alert:t.saveModalAlert,isVisible:t.isVisible}}))(Dt));var Nt=a(150361),Ot=a.n(Nt),It=a(701469),At=a.n(It),$t=a(357179),Rt=a(690233),Mt=a(727034),jt=a(642753),Ut=a(699963);const Lt=N.iK.div`
  ${({theme:e})=>O.iv`
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    height: ${6*e.gridUnit}px;
    padding: 0 ${e.gridUnit}px;

    // hack to make the drag preview image corners rounded
    transform: translate(0, 0);
    background-color: inherit;
    border-radius: 4px;

    > div {
      min-width: 0;
      margin-right: ${2*e.gridUnit}px;
    }
  `}
`;function zt(e){const{labelRef:t,showTooltip:a,type:r,value:o}=e,[{isDragging:n},s]=(0,Mt.c)({item:{value:e.value,type:e.type},collect:e=>({isDragging:e.isDragging()})}),i={labelRef:t,showTooltip:!n&&a,showType:!0};return(0,O.tZ)(Lt,{"data-test":"DatasourcePanelDragOption",ref:s},r===jt.g.Column?(0,O.tZ)(Ut.l,w()({column:o},i)):(0,O.tZ)(Ut.B,w()({metric:o},i)),(0,O.tZ)(z.Z.Drag,null))}var qt=a(591665);const Pt=(0,pe.cr)(me.T.ENABLE_EXPLORE_DRAG_AND_DROP),Ft=N.iK.button`
  background: none;
  border: none;
  text-decoration: underline;
  color: ${({theme:e})=>e.colors.primary.dark1};
`,Qt=N.iK.div`
  text-align: center;
  padding-top: 2px;
`,Kt=N.iK.div`
  ${({theme:e})=>O.iv`
    background-color: ${e.colors.grayscale.light5};
    position: relative;
    height: 100%;
    display: flex;
    flex-direction: column;
    max-height: 100%;
    .ant-collapse {
      height: auto;
    }
    .field-selections {
      padding: 0 0 ${4*e.gridUnit}px;
      overflow: auto;
    }
    .field-length {
      margin-bottom: ${2*e.gridUnit}px;
      font-size: ${e.typography.sizes.s}px;
      color: ${e.colors.grayscale.light1};
    }
    .form-control.input-md {
      width: calc(100% - ${8*e.gridUnit}px);
      height: ${8*e.gridUnit}px;
      margin: ${2*e.gridUnit}px auto;
    }
    .type-label {
      font-size: ${e.typography.sizes.s}px;
      color: ${e.colors.grayscale.base};
    }
    .Control {
      padding-bottom: 0;
    }
  `};
`,Vt=N.iK.div`
  display: flex;
  justify-content: center;
  align-items: center;
  color: ${({theme:e})=>e.colors.grayscale.base};
`,Bt=N.iK.div`
  ${({theme:e})=>O.iv`
    overflow: hidden;
    text-overflow: ellipsis;
    font-size: ${e.typography.sizes.s}px;
    background-color: ${e.colors.grayscale.light4};
    margin: ${2*e.gridUnit}px 0;
    border-radius: 4px;
    padding: 0 ${e.gridUnit}px;

    &:first-of-type {
      margin-top: 0;
    }
    &:last-of-type {
      margin-bottom: 0;
    }

    ${Pt&&O.iv`
      padding: 0;
      cursor: pointer;
      &:hover {
        background-color: ${e.colors.grayscale.light3};
      }
    `}

    & > span {
      white-space: nowrap;
    }

    .option-label {
      display: inline;
    }

    .metric-option {
      & > svg {
        min-width: ${4*e.gridUnit}px;
      }
      & > .option-label {
        overflow: hidden;
        text-overflow: ellipsis;
      }
    }
  `}
`,Ht=N.iK.span`
  ${({theme:e})=>`\n    font-size: ${e.typography.sizes.m}px;\n    line-height: 1.3;\n  `}
`,Wt=N.iK.div`
  ${({theme:e})=>O.iv`
    margin: 0 ${2.5*e.gridUnit}px;

    span {
      text-decoration: underline;
    }
  `}
`,Jt=N.iK.div`
  ${({theme:e})=>O.iv`
    padding: 0px 10px;
  `}
`,Yt=e=>{const t={labelRef:(0,r.useRef)(null)};return(0,O.tZ)(Bt,{className:e.className},r.cloneElement(e.children,t))};function Gt({datasource:e,formData:t,controls:{datasource:a},actions:o,shouldForceUpdate:n}){var s;const{columns:l,metrics:c,categories:d=[]}=e,u=(0,r.useMemo)((()=>[...At()(l)?l:[]].sort(((e,t)=>null==e||!e.is_dttm||null!=t&&t.is_dttm?null==t||!t.is_dttm||null!=e&&e.is_dttm?0:1:-1))),[l]),[p,m]=(0,r.useState)(!1),[g,f]=(0,r.useState)(""),[v,b]=(0,r.useState)([]),[y,S]=(0,r.useState)([]),[_,Z]=(0,r.useState)([]),[x,k]=(0,r.useState)(!0),[C,D]=(0,r.useState)({columns:u,metrics:c}),[E,N]=(0,r.useState)(!1),[I,A]=(0,r.useState)(!1),[$,R]=(0,r.useState)(!1);(0,r.useEffect)((()=>{var e,t,a;const r=null==d||null==(e=d[0])?void 0:e.id,o=null==d||null==(t=d[0])?void 0:t.category_type,s=null==d||null==(a=d[0])?void 0:a.is_fast_filter;if(r){const e={category_id:r};R(!0),de.Z.post({endpoint:"api/v1/sqllab/execute/get_columns_values/",headers:{"Content-Type":"application/json"},body:JSON.stringify(e)}).then((({json:e})=>{R(!1);const t=(0,$t.$)(e||[],["first_cate","second_cate","field_code"],(e=>{if(s&&(null!=e&&e.column_name||"field_code"!==(null==e?void 0:e.nodeType)||(e.column_name=e.field_code,e.groupby=!0,e.advanced_data_type=null,e.certification_details=null,e.certified_by=null,e.description=null,e.expression=null,e.filterable=!0,e.id=Math.floor(9e4*Math.random())+1e4,e.is_certified=!1,e.is_dttm=!1,e.python_date_format=null,e.type="BLOB",e.verbose_name="",e.warning_markdown=null)),"simpled"===o){let t=null;return t=e.column_name?(0,O.tZ)(Yt,{key:e.column_name+String(n),className:"column"},(0,O.tZ)(zt,{value:e,type:jt.g.Column})):(0,O.tZ)("div",{style:{cursor:"not-allowed"},draggable:!0,title:null==e?void 0:e.field_code},null==e?void 0:e.field_code),t}return(0,O.tZ)(Yt,{key:(null==e?void 0:e.column_name)+String(n),className:"column"},Pt?(0,O.tZ)(zt,{value:e,type:jt.g.Column}):(0,O.tZ)(Ut.l,{column:e,showType:!0}))}),u,!0,"column_name");b(t)})).catch((e=>{R(!1)}))}}),[]);const M=(0,r.useMemo)((()=>T()((e=>{Q(e),D(""!==e?{columns:(0,Rt.Lu)(u,e,{keys:[{key:"verbose_name",threshold:Rt.tL.CONTAINS},{key:"column_name",threshold:Rt.tL.CONTAINS},{key:e=>{var t,a;return[null!=(t=null==e?void 0:e.description)?t:"",null!=(a=null==e?void 0:e.expression)?a:""].map((e=>(null==e?void 0:e.replace(/[_\n\s]+/g," "))||""))},threshold:Rt.tL.CONTAINS,maxRanking:Rt.tL.CONTAINS}],keepDiacritics:!0}),metrics:(0,Rt.Lu)(c,e,{keys:[{key:"verbose_name",threshold:Rt.tL.CONTAINS},{key:"metric_name",threshold:Rt.tL.CONTAINS},{key:e=>{var t,a;return[null!=(t=null==e?void 0:e.description)?t:"",null!=(a=null==e?void 0:e.expression)?a:""].map((e=>(null==e?void 0:e.replace(/[_\n\s]+/g," "))||""))},threshold:Rt.tL.CONTAINS,maxRanking:Rt.tL.CONTAINS}],keepDiacritics:!0,baseSort:(e,t)=>{var a,r,o,n,s,i;return Number(null!=(a=null==t||null==(r=t.item)?void 0:r.is_certified)?a:0)-Number(null!=(o=null==e||null==(n=e.item)?void 0:n.is_certified)?o:0)||String(null!=(s=null==e?void 0:e.rankedValue)?s:"").localeCompare(null!=(i=null==t?void 0:t.rankedValue)?i:"")}})}:{columns:u,metrics:c})}),h.oP)),[u,c,v]);(0,r.useEffect)((()=>{D({columns:u,metrics:c}),f("")}),[u,e,c]);const j=e=>e.sort(((e,t)=>{var a,r;return(null!=(a=null==t?void 0:t.is_certified)?a:0)-(null!=(r=null==e?void 0:e.is_certified)?r:0)})),U=(0,r.useMemo)((()=>{var e;return E?null==C?void 0:C.metrics:null==C||null==(e=C.metrics)||null==e.slice?void 0:e.slice(0,50)}),[null==C?void 0:C.metrics,E]),L=(0,r.useMemo)((()=>{var e;return j(I?null==C?void 0:C.columns:null==C||null==(e=C.columns)||null==e.slice?void 0:e.slice(0,50))}),[C.columns,I]),q={query:le.i9.Query,saved_query:le.i9.SavedQuery},P=e.type&&q[e.type],F=e=>{Z(e),k(!1)},Q=e=>{if(Z([]),S([]),e){const t=Ot()(v),a=[],r=[];t.forEach((t=>{const o=(null==t?void 0:t.children)||[],n=[];o.forEach((a=>{const o=((null==a?void 0:a.children)||[]).filter((o=>{var n;return((null==o||null==(n=o.column_name)?void 0:n.indexOf(e))>-1||(null==o?void 0:o[null==o?void 0:o.nodeType].indexOf(e))>-1)&&(r.push(null==o?void 0:o.key),r.push(null==a?void 0:a.key),r.push(null==t?void 0:t.key),!0)}));o.length>0&&(a.children=o,n.push(a))})),n.length>0&&(t.children=n,a.push(t))}));const o=Array.from(new Set(r));Z(o),S(a),k(!0)}else Z([]),S([]),k(!0)},K=(0,r.useMemo)((()=>{var e;return(0,O.tZ)(r.Fragment,null,(0,O.tZ)(St.II,{allowClear:!0,onChange:e=>{f(e.target.value),M(e.target.value)},value:g,prefix:(0,O.tZ)(Vt,null,(0,O.tZ)(z.Z.Search,{iconSize:"m"})),className:"form-control input-md",placeholder:(0,i.t)("Search Metrics & Columns")}),(0,O.tZ)("div",{className:"field-selections"},P&&"false"!==sessionStorage.getItem("showInfobox")&&(0,O.tZ)(Wt,null,(0,O.tZ)(ge.Z,{closable:!0,onClose:()=>sessionStorage.setItem("showInfobox","false"),type:"info",message:"",description:(0,O.tZ)(r.Fragment,null,(0,O.tZ)("span",{role:"button",tabIndex:0,onClick:()=>m(!0),className:"add-dataset-alert-description"},(0,i.t)("Create a dataset")),(0,i.t)(" to edit or add columns and metrics."))})),(0,O.tZ)(at.Z,{defaultActiveKey:["metrics","column"],expandIconPosition:"right",ghost:!0},(null==c?void 0:c.length)&&(0,O.tZ)(at.Z.Panel,{header:(0,O.tZ)(Ht,null,(0,i.t)("Metrics")),key:"metrics"},(0,O.tZ)("div",{className:"field-length"},(0,i.t)("Showing %s of %s",null==U?void 0:U.length,null==C?void 0:C.metrics.length)),null==U||null==U.map?void 0:U.map((e=>(0,O.tZ)(Yt,{key:e.metric_name+String(n),className:"column"},Pt?(0,O.tZ)(zt,{value:e,type:jt.g.Metric}):(0,O.tZ)(Ut.B,{metric:e,showType:!0})))),(null==C||null==(e=C.metrics)?void 0:e.length)>50?(0,O.tZ)(Qt,null,(0,O.tZ)(Ft,{onClick:()=>N(!E)},E?(0,i.t)("Show less..."):(0,i.t)("Show all..."))):(0,O.tZ)(r.Fragment,null)),v.length>1?(0,O.tZ)(Jt,null,g?_.length&&y.length?(0,O.tZ)(qt.Z,{key:"okfilter",onExpand:F,expandedKeys:_,autoExpandParent:x,treeData:y}):(0,O.tZ)(qt.Z,{key:"datafilter",treeData:y}):(0,O.tZ)(qt.Z,{key:"fulltree",blockNode:!0,treeData:v})):(0,O.tZ)(at.Z.Panel,{header:(0,O.tZ)(Ht,null,(0,i.t)("Columns")),key:"column"},(0,O.tZ)("div",{className:"field-length"},(0,i.t)("Showing %s of %s",L.length,C.columns.length)),L.map((e=>(0,O.tZ)(Yt,{key:e.column_name+String(n),className:"column"},Pt?(0,O.tZ)(zt,{value:e,type:jt.g.Column}):(0,O.tZ)(Ut.l,{column:e,showType:!0})))),C.columns.length>50?(0,O.tZ)(Qt,null,(0,O.tZ)(Ft,{onClick:()=>A(!I)},I?(0,i.t)("Show Less..."):(0,i.t)("Show all..."))):(0,O.tZ)(r.Fragment,null)))))}),[L,g,C.columns.length,null==C||null==(s=C.metrics)?void 0:s.length,U,M,I,E,P,n,v,$,_,x]);return(0,O.tZ)(Kt,null,P&&p&&(0,O.tZ)(fe.W,{visible:p,onHide:()=>m(!1),buttonTextOnSave:(0,i.t)("Save"),buttonTextOnOverwrite:(0,i.t)("Overwrite"),datasource:(0,ve.z)(e),openWindow:!1,formData:t}),(0,O.tZ)(st.Z,w()({},a,{name:"datasource",actions:o})),null!=e.id&&K)}var Xt=a(328062),ea=a(441609),ta=a.n(ea),aa=a(618446),ra=a.n(aa),oa=a(288306),na=a.n(oa),sa=a(338575),ia=a(692252);const la=na()(((e,t)=>{const a={};return((null==t?void 0:t.controlPanelSections)||[]).filter(sa.D_).forEach((e=>{e.controlSetRows.forEach((e=>{e.forEach((e=>{e&&("string"===typeof e?a[e]=ia.ai[e]:e.name&&e.config&&(a[e.name]=e.config))}))}))})),a})),ca=e=>{const t=(0,We.Z)().get(e);return la(e,t)};var da=a(309679),ua=a(601304),ha=a(676962);const pa={origFormData:D().object.isRequired,currentFormData:D().object.isRequired},ma=N.iK.span`
  ${({theme:e})=>`\n    font-size: ${e.typography.sizes.s}px;\n    color: ${e.colors.grayscale.dark1};\n    background-color: ${e.colors.alert.base};\n\n    &: hover {\n      background-color: ${e.colors.alert.dark1};\n    }\n  `}
`,ga=(0,N.iK)(ha.Z)`
  .table-cell {
    vertical-align: unset !important;
  }
`;function fa(e){if(void 0===e||null===e||""===e)return null;if("object"===typeof e){if(Array.isArray(e)&&0===e.length)return null;const t=Object.keys(e);if(t&&0===t.length)return null}return e}class va extends r.Component{constructor(e){super(e);const t=this.getDiffs(e),a=ca(this.props.origFormData.viz_type),r=this.getRowsFromDiffs(t,a);this.state={rows:r,hasDiffs:!ta()(t),controlsMap:a}}UNSAFE_componentWillReceiveProps(e){if(ra()(this.props,e))return;const t=this.getDiffs(e);this.setState((e=>({rows:this.getRowsFromDiffs(t,e.controlsMap),hasDiffs:!ta()(t)})))}getRowsFromDiffs(e,t){return Object.entries(e).map((([e,a])=>({control:t[e]&&t[e].label||e,before:this.formatValue(a.before,e,t),after:this.formatValue(a.after,e,t)})))}getDiffs(e){const t=(0,Y.BR)(e.origFormData),a=(0,Y.BR)(e.currentFormData),r=Object.keys(a),o={};return r.forEach((e=>{(t[e]||a[e])&&(["filters","having","having_filters","where"].includes(e)||this.isEqualish(t[e],a[e])||(o[e]={before:t[e],after:a[e]}))})),o}isEqualish(e,t){return ra()(fa(e),fa(t))}formatValue(e,t,a){var r,o,n,s;if(void 0===e)return"N/A";if(null===e)return"null";if("AdhocFilterControl"===(null==(r=a[t])?void 0:r.type))return e.length?e.map((e=>{const t=e.comparator&&e.comparator.constructor===Array?`[${e.comparator.join(", ")}]`:e.comparator;return`${e.subject} ${e.operator} ${t}`})).join(", "):"[]";if("BoundsControl"===(null==(o=a[t])?void 0:o.type))return`Min: ${e[0]}, Max: ${e[1]}`;if("CollectionControl"===(null==(n=a[t])?void 0:n.type))return e.length?(0,da.o)(e,2):"[]";if("MetricsControl"===(null==(s=a[t])?void 0:s.type)&&e.constructor===Array){const t=e.map((e=>{var t;return null!=(t=null==e?void 0:e.label)?t:e}));return t.length?(0,da.o)(t,2):"[]"}if("boolean"===typeof e)return e?"true":"false";if(e.constructor===Array){const t=e.map((e=>{var t;return null!=(t=null==e?void 0:e.label)?t:e}));return t.length?(0,da.o)(t,2):"[]"}return"string"===typeof e||"number"===typeof e?e:(0,da.o)(e,2)}renderModalBody(){const e=[{accessor:"control",Header:(0,i.t)("Control")},{accessor:"before",Header:(0,i.t)("Before"),Cell:({value:e})=>(0,O.tZ)("pre",null,e)},{accessor:"after",Header:(0,i.t)("After"),Cell:({value:e})=>(0,O.tZ)("pre",null,e)}];return(0,O.tZ)(ga,{columns:e,data:this.state.rows,pageSize:50,className:"table-condensed",columnsForWrapText:["Control","Before","After"]})}renderTriggerNode(){return(0,O.tZ)(j.u,{id:"difference-tooltip",title:(0,i.t)("Click to see difference")},(0,O.tZ)(ma,{className:"label"},(0,i.t)("Altered")))}render(){return this.state.hasDiffs?(0,O.tZ)(ua.Z,{triggerNode:this.renderTriggerNode(),modalTitle:(0,i.t)("Chart changes"),modalBody:this.renderModalBody(),responsive:!0}):null}}va.propTypes=pa;var ba=a(983673),ya=a(852564),Sa=a(159507),_a=a(596022);const wa={actions:D().object.isRequired,canOverwrite:D().bool.isRequired,canDownload:D().bool.isRequired,dashboardId:D().number,isStarred:D().bool.isRequired,slice:D().object,sliceName:D().string,table_name:D().string,formData:D().object,ownState:D().object,timeout:D().number,chart:W.$6,saveDisabled:D().bool},Za=e=>O.iv`
  color: ${e.colors.primary.dark2};
  & > span[role='img'] {
    margin-right: 0;
  }
`,xa=e=>O.iv`
  display: flex;
  align-items: center;
  margin-left: ${e.gridUnit}px;
  & > span {
    margin-right: ${3*e.gridUnit}px;
  }
`,ka=({dashboardId:e,slice:t,actions:a,formData:n,ownState:s,chart:l,user:c,canOverwrite:d,canDownload:u,isStarred:h,sliceName:p,saveDisabled:m,metadata:g,onSaveChart:f})=>{const v=(0,o.I0)(),{latestQueryFormData:b,sliceFormData:y}=l,[S,_]=(0,r.useState)(!1);(0,r.useEffect)((()=>{e&&(async()=>{const{dashboards:t}=g||{},a=e&&t&&t.find((t=>t.id===e));if(a)try{var r;const e=await de.Z.get({endpoint:`/api/v1/dashboard/${a.id}`}),t=null==e||null==(r=e.json)?void 0:r.result,o=JSON.parse(t.json_metadata),n=o.shared_label_colors||{},s=o.label_colors||{},i={...n,...s},l=Xt.getNamespace();Object.keys(i).forEach((e=>{l.setColor(e,i[e],o.color_scheme)}))}catch(e){I.Z.info((0,i.t)("Unable to retrieve dashboard colors"))}})()}),[]);const w=(0,r.useCallback)((()=>{v((0,ae.setSaveChartModalVisibility)(!0))}),[v]),Z=(0,r.useCallback)((e=>{v((0,te.sliceUpdated)(e))}),[v]),[x,k,T]=(0,_a.gT)(b,u,t,a.redirectSQLLab,(()=>{_(!0)}),s,null==g?void 0:g.dashboards),C=(0,r.useMemo)((()=>{if(!g)return null;const e=[];return e.push({type:Sa.pG.DASHBOARDS,title:g.dashboards.length>0?(0,i.tn)("Added to 1 dashboard","Added to %s dashboards",g.dashboards.length,g.dashboards.length):(0,i.t)("Not added to any dashboard"),description:g.dashboards.length>0?(0,i.t)("You can preview the list of dashboards in the chart settings dropdown."):void 0}),e.push({type:Sa.pG.LAST_MODIFIED,value:g.changed_on_humanized,modifiedBy:g.changed_by||(0,i.t)("Not available")}),e.push({type:Sa.pG.OWNER,createdBy:g.created_by||(0,i.t)("Not available"),owners:g.owners.length>0?g.owners:(0,i.t)("None"),createdOn:g.created_on_humanized}),null!=t&&t.description&&e.push({type:Sa.pG.DESCRIPTION,value:null==t?void 0:t.description}),(0,O.tZ)(Sa.ZP,{items:e,tooltipPlacement:"bottom"})}),[g,null==t?void 0:t.description]),D=null==t?void 0:t.slice_name;return(0,O.tZ)(r.Fragment,null,(0,O.tZ)(ya.u,{editableTitleProps:{title:p,canEdit:!t||d||((null==t?void 0:t.owners)||[]).includes(null==c?void 0:c.userId),onSave:a.updateChartTitle,placeholder:(0,i.t)("Add the name of the chart"),label:(0,i.t)("Chart title")},showTitlePanelItems:!!t,certificatiedBadgeProps:{certifiedBy:null==t?void 0:t.certified_by,details:null==t?void 0:t.certification_details},showFaveStar:!(null==c||!c.userId),faveStarProps:{itemId:null==t?void 0:t.slice_id,fetchFaveStar:a.fetchFaveStar,saveFaveStar:a.saveFaveStar,isStarred:h,showTooltip:!0},titlePanelAdditionalItems:(0,O.tZ)("div",{css:xa},y?(0,O.tZ)(va,{className:"altered",origFormData:{...y,chartTitle:D},currentFormData:{...n,chartTitle:p}}):null,C),rightPanelAdditionalItems:(0,O.tZ)(j.u,{title:m?(0,i.t)("Add required control values to save chart"):null},(0,O.tZ)("div",null,(0,O.tZ)(Ne.Z,{buttonStyle:"secondary",onClick:w,disabled:m,"data-test":"query-save-button",css:Za},(0,O.tZ)(z.Z.SaveOutlined,{iconSize:"l"}),(0,i.t)("Save")))),additionalActionsMenu:x,menuDropdownProps:{visible:k,onVisibleChange:T}}),S&&(0,O.tZ)(ba.Z,{show:S,onHide:()=>{_(!1)},onSave:Z,slice:t}))};ka.propTypes=wa;const Ta=ka,Ca={actions:D().object.isRequired,onQuery:D().func,can_overwrite:D().bool.isRequired,can_download:D().bool.isRequired,datasource:D().object,dashboardId:D().number,column_formats:D().object,containerId:D().string.isRequired,isStarred:D().bool.isRequired,slice:D().object,sliceName:D().string,table_name:D().string,vizType:D().string.isRequired,form_data:D().object,ownState:D().object,standalone:D().bool,force:D().bool,timeout:D().number,chartIsStale:D().bool,chart:W.$6,errorMessage:D().node,triggerRender:D().bool},Da=[100,0],Ea=({chart:e,slice:t,vizType:a,ownState:o,triggerRender:n,force:s,datasource:i,errorMessage:l,form_data:c,onQuery:d,actions:u,timeout:h,standalone:p,chartIsStale:m,chartAlert:g})=>{var f;const v=(0,N.Fg)(),b=1.25*v.gridUnit,{width:y,height:S,ref:_}=(v.gridUnit,(0,ue.NB)({refreshMode:"debounce",refreshRate:300})),[w,Z]=(0,r.useState)((0,pe.cr)(me.T.DATAPANEL_CLOSED_BY_DEFAULT)?Da:(0,q.rV)(q.dR.chart_split_sizes,Da)),[x,k]=(0,r.useState)(!(0,pe.cr)(me.T.DATAPANEL_CLOSED_BY_DEFAULT)&&(0,q.rV)(q.dR.is_datapanel_open,!1)),[T,C]=(0,r.useState)(!1),D=(0,ie.Z)(),{useLegacyApi:E}=null!=(f=D.get(a))?f:{},I=E&&i.type!==le.i9.Table,A=!g&&m&&!I&&"failed"!==e.chartStatus&&(0,ce.Z)(e.queriesResponse).length>0,$=(0,r.useCallback)((async function(){if(t&&null===t.query_context){const e=(0,X.u)({formData:t.form_data,force:s,resultFormat:"json",resultType:"full",setDataMask:null,ownState:null});await de.Z.put({endpoint:`/api/v1/chart/${t.slice_id}`,headers:{"Content-Type":"application/json"},body:JSON.stringify({query_context:JSON.stringify(e),query_context_generation:!0})})}}),[t]);(0,r.useEffect)((()=>{$()}),[$]),(0,r.useEffect)((()=>{(0,q.LS)(q.dR.chart_split_sizes,w)}),[w]);(0,r.useCallback)((e=>{Z(e)}),[]);const R=(0,r.useCallback)((()=>{u.setForceQuery(!0),u.postChartFormData(c,!0,h,e.id,void 0,o),u.updateQueryFormData(c,e.id)}),[u,e.id,c,o,h]),M=((0,r.useCallback)((e=>{let t;t=e?[60,40]:Da,Z(t),k(e)}),[]),(0,r.useCallback)((()=>(0,O.tZ)("div",{css:O.iv`
          min-height: 0;
          flex: 1;
          overflow: hidden;
        `,ref:_},y&&(0,O.tZ)(he.Z,{width:Math.floor(y),ownState:o,annotationData:e.annotationData,chartAlert:e.chartAlert,chartStackTrace:e.chartStackTrace,chartId:e.id,chartStatus:e.chartStatus,triggerRender:n,force:s,datasource:i,errorMessage:l,formData:c,latestQueryFormData:e.latestQueryFormData,onQuery:d,queriesResponse:e.queriesResponse,chartIsStale:m,setControlValue:u.setControlValue,timeout:h,triggerQuery:e.triggerQuery,vizType:a}))),[u.setControlValue,e.annotationData,e.chartAlert,e.chartStackTrace,e.chartStatus,e.id,e.latestQueryFormData,e.queriesResponse,e.triggerQuery,m,S,_,y,i,l,s,c,d,o,h,n,a])),j=(0,r.useMemo)((()=>(0,O.tZ)(r.Fragment,null,M())),[A,l,d,e.queriesResponse,e.chartStatus,e.chartUpdateStartTime,e.chartUpdateEndTime,R,null==c?void 0:c.row_limit,M]),U=(0,r.useMemo)((()=>M()),[M]),[L,z]=(0,r.useState)(e.latestQueryFormData);(0,r.useEffect)((()=>{n||z(e.latestQueryFormData)}),[e.latestQueryFormData]);(0,r.useCallback)(((e,t,a)=>({[e]:`calc(${t}% - ${a+b}px)`})),[b]);if(p){const e="background-transparent";return document.body.className.split(" ").includes(e)||(document.body.className+=` ${e}`),U}return(0,O.tZ)(r.Fragment,null,j)};Ea.propTypes=Ca;const Na=Ea,Oa={...Qe.propTypes,actions:D().object.isRequired,datasource_type:D().string.isRequired,dashboardId:D().number,isDatasourceMetaLoading:D().bool.isRequired,chart:W.$6.isRequired,slice:D().object,sliceName:D().string,controls:D().object.isRequired,forcedHeight:D().string,form_data:D().object.isRequired,standalone:D().bool.isRequired,force:D().bool,timeout:D().number,impressionId:D().string,vizType:D().string,saveAction:D().string,isSaveModalVisible:D().bool},Ia=N.iK.div`
  display: flex;
  flex-direction: column;
  height: 100%;
  min-height: 0;
`,Aa=N.iK.div`
  ${({theme:e})=>O.iv`
    background: ${e.colors.grayscale.light5};
    text-align: left;
    position: relative;
    width: 100%;
    max-height: 100%;
    min-height: 0;
    display: flex;
    flex: 1;
    flex-wrap: nowrap;
    border-top: 1px solid ${e.colors.grayscale.light2};
    .explore-column {
      display: flex;
      flex-direction: column;
      padding: ${2*e.gridUnit}px 0;
      max-height: 100%;
    }
    .data-source-selection {
      background-color: ${e.colors.grayscale.light5};
      padding: ${2*e.gridUnit}px 0;
      border-right: 1px solid ${e.colors.grayscale.light2};
    }
    .main-explore-content {
      flex: 1;
      min-width: ${128*e.gridUnit}px;
      border-left: 1px solid ${e.colors.grayscale.light2};
      padding: 0 ${4*e.gridUnit}px;
      .panel {
        margin-bottom: 0;
      }
    }
    .controls-column {
      align-self: flex-start;
      padding: 0;
    }
    .title-container {
      position: relative;
      display: flex;
      flex-direction: row;
      padding: 0 ${2*e.gridUnit}px 0 ${4*e.gridUnit}px;
      justify-content: space-between;
      .horizontal-text {
        font-size: ${e.typography.sizes.m}px;
      }
    }
    .no-show {
      display: none;
    }
    .vertical-text {
      writing-mode: vertical-rl;
      text-orientation: mixed;
    }
    .sidebar {
      height: 100%;
      background-color: ${e.colors.grayscale.light4};
      padding: ${2*e.gridUnit}px;
      width: ${8*e.gridUnit}px;
    }
    .collapse-icon > svg {
      color: ${e.colors.primary.base};
    }
    .action-button {
      padding: 3px;
      border-radius: 3px;
      transition: 0.1s;
      cursor: pointer;
      &:hover {
        color: ${e.colors.primary.base};
        background-color: ${e.colors.grayscale.light3};
      }
    }
  `};
`;T()((async(e,t,a,r,o,n,s,i)=>{const l={...e},c=e.slice_id,d=new URLSearchParams(window.location.search),p=Object.fromEntries(d);c?p[h.KD.sliceId.name]=c:(p[h.KD.datasourceId.name]=t,p[h.KD.datasourceType.name]=a);const m=(null==l?void 0:l.url_params)||{};Object.entries(m).forEach((([e,t])=>{h.$O.includes(e)||(p[e]=t)}));try{let d,m;if(r?(d=await(0,Y.nv)(t,a,e,c,i),m="replaceState"):(d=(0,u.eY)(h.KD.formDataKey),await(0,Y.LW)(t,a,d,e,c,i),m="pushState"),(0,$.Rs)(window.location.pathname).startsWith("/explore")){const e=(0,X.y8)(o?h.KD.standalone.name:null,{[h.KD.formDataKey.name]:d,...p},n);window.history[m](l,s,e)}}catch(e){I.Z.warn("Failed at altering browser history",e)}}),1e3);function $a(e){const t=(0,M.gp)().dynamicPlugins[e.vizType],a=t&&t.mounting,o=(0,U.D)(a),n=(0,U.D)(e.controls),[s,l]=(0,r.useState)(e.controls),{drilldownColumns:c,enableDrilldown:d}=e.controls,[u,h]=(0,r.useState)(!1),[p,m]=(0,r.useState)(-1),g=(0,oe.z)(),f=(0,N.Fg)(),v={controls_width:320,datasource_width:250},b=(0,r.useCallback)((async({isReplace:t=!1,title:a}={})=>{e.dashboardId?(e.form_data,e.dashboardId):e.form_data;const{id:r,type:o}=e.datasource}),[e.dashboardId,e.form_data,e.datasource.id,e.datasource.type,e.standalone,e.force,g]),y=(0,r.useCallback)((()=>{const t=window.history.state;t&&Object.keys(t).length&&(e.actions.setExploreControls(t),e.actions.postChartFormData(t,e.force,e.timeout,e.chart.id))}),[e.actions,e.chart.id,e.timeout]),S=(0,r.useCallback)((()=>{e.actions.setForceQuery(!1),e.actions.triggerQuery(!0,e.chart.id),b(),l(e.controls)}),[e.controls,b,e.actions,e.chart.id]),_=(0,r.useCallback)((t=>{if(t.ctrlKey||t.metaKey){const a="Enter"===t.key||13===t.keyCode,r="s"===t.key||83===t.keyCode;a?S():r&&e.slice&&e.actions.saveSlice(e.form_data,{action:"overwrite",slice_id:e.slice.slice_id,slice_name:e.slice.slice_name,add_to_dash:"noSave",goto_dash:!1}).then((({data:e})=>{window.location=e.slice.slice_url}))}}),[S,e.actions,e.form_data,e.slice]);function Z(){h(!u)}(0,L.J)((()=>{e.actions.logEvent(Q.$b)})),(0,R.S)(g,((e,t)=>{t&&b({isReplace:!0})}));const k=(0,U.D)(y);(0,r.useEffect)((()=>(k&&window.removeEventListener("popstate",k),window.addEventListener("popstate",y),()=>{window.removeEventListener("popstate",y)})),[y,k]);const T=(0,U.D)(_);(0,r.useEffect)((()=>(T&&window.removeEventListener("keydown",T),document.addEventListener("keydown",_),()=>{document.removeEventListener("keydown",_)})),[_,T]),(0,r.useEffect)((()=>{o&&!a&&e.actions.dynamicPluginControlsReady()}),[a]),(0,r.useEffect)((()=>{Object.values(e.controls).some((e=>e.validationErrors&&e.validationErrors.length>0))||e.actions.triggerQuery(!0,e.chart.id)}),[]);const C=(0,r.useCallback)((t=>{const a=t?{...e.chart.latestQueryFormData,...(0,ee.Hu)(x()(e.controls,t))}:(0,ee.Hu)(e.controls);e.actions.updateQueryFormData(a,e.chart.id),e.actions.renderTriggered((new Date).getTime(),e.chart.id),b()}),[b,e.actions,e.chart.id,e.chart.latestQueryFormData,e.controls]);(0,r.useEffect)((()=>{if(n&&e.chart.latestQueryFormData.viz_type===e.controls.viz_type.value){!e.controls.datasource||null!=n.datasource&&e.controls.datasource.value===n.datasource.value||(0,H.QR)(e.form_data.datasource,!0);const t=Object.keys(e.controls).filter((t=>"undefined"!==typeof n[t]&&!(0,P.JB)(e.controls[t].value,n[t].value))).filter((t=>e.controls[t].renderTrigger));t.length>0&&C(t)}}),[e.controls,e.ownState]);const D=(0,r.useMemo)((()=>{if(s){return Object.keys(e.controls).filter((t=>"undefined"!==typeof s[t]&&!(0,P.JB)(e.controls[t].value,s[t].value))).some((t=>!e.controls[t].renderTrigger&&!e.controls[t].dontRefreshOnChange))}return!1}),[s,e.controls]);(0,R.S)(e.saveAction,(()=>{["saveas","overwrite"].includes(e.saveAction)&&(S(),b({isReplace:!0}),e.actions.setSaveAction(null))})),(0,r.useEffect)((()=>{void 0!==e.ownState&&(S(),C())}),[e.ownState]),D&&e.actions.logEvent(Q.Ep);const E=(0,r.useMemo)((()=>{const t=Object.values(e.controls).filter((e=>e.validationErrors&&e.validationErrors.length>0));if(0===t.length)return null;const a=t.map((e=>e.validationErrors)),r=[...new Set(a.flat())].map((e=>[t.filter((t=>{var a;return null==(a=t.validationErrors)?void 0:a.includes(e)})).map((e=>e.label)),e])).map((([e,t])=>(0,O.tZ)("div",{key:t},e.length>1?(0,i.t)("Controls labeled "):(0,i.t)("Control labeled "),(0,O.tZ)("strong",null,` ${e.join(", ")}`),(0,O.tZ)("span",null,": ",t))));let o;return r.length>0&&(o=(0,O.tZ)("div",{style:{textAlign:"left"}},r)),o}),[e.controls]);function I(){return(0,O.tZ)(Qe,w()({},e,{errorMessage:E,chartIsStale:D,onQuery:S}))}function $(e){return(0,q.rV)(e,v[e])}function F(e,t){const a=Number($(e))+t.width;(0,q.LS)(e,a)}return window.location.pathname.indexOf("/explore/p")>-1?(0,O.tZ)("div",{style:{padding:"20px 50px"}},(0,O.tZ)(Na,w()({},e,{errorMessage:E,chartIsStale:D,onQuery:S}))):e.standalone?I():(0,O.tZ)(Ia,null,(0,O.tZ)(Ta,{actions:e.actions,canOverwrite:e.can_overwrite,canDownload:e.can_download,dashboardId:e.dashboardId,isStarred:e.isStarred,slice:e.slice,sliceName:e.sliceName,table_name:e.table_name,formData:e.form_data,chart:e.chart,ownState:e.ownState,user:e.user,reports:e.reports,saveDisabled:!!E||"loading"===e.chart.chartStatus,metadata:e.metadata}),(0,O.tZ)(Aa,{id:"explore-container"},(0,O.tZ)(O.xB,{styles:O.iv`
            .navbar {
              margin-bottom: 0;
            }
            body {
              height: 100vh;
              max-height: 100vh;
              overflow: hidden;
            }
            #app-menu,
            #app {
              flex: 1 1 auto;
            }
            #app {
              flex-basis: 100%;
              overflow: hidden;
              height: 100%;
            }
            #app-menu {
              flex-shrink: 0;
            }
          `}),(0,O.tZ)(A.e,{onResizeStop:(e,t,a,r)=>{m(null==r?void 0:r.width),F(q.dR.datasource_width,r)},defaultSize:{width:$(q.dR.datasource_width),height:"100%"},minWidth:v[q.dR.datasource_width],maxWidth:"33%",enable:{right:!0},className:u?"no-show":"explore-column data-source-selection"},(0,O.tZ)("div",{className:"title-container"},(0,O.tZ)("span",{className:"horizontal-text"},(0,i.t)("Chart Source")),(0,O.tZ)("span",{role:"button",tabIndex:0,className:"action-button",onClick:Z},(0,O.tZ)(z.Z.Expand,{className:"collapse-icon",iconColor:f.colors.primary.base,iconSize:"l"}))),(0,O.tZ)(Gt,{formData:e.form_data,datasource:e.datasource,controls:e.controls,actions:e.actions,shouldForceUpdate:p,user:e.user})),u?(0,O.tZ)("div",{className:"sidebar",onClick:Z,"data-test":"open-datasource-tab",role:"button",tabIndex:0},(0,O.tZ)("span",{role:"button",tabIndex:0,className:"action-button"},(0,O.tZ)(j.u,{title:(0,i.t)("Open Datasource tab")},(0,O.tZ)(z.Z.Collapse,{className:"collapse-icon",iconColor:f.colors.primary.base,iconSize:"l"})))):null,(0,O.tZ)(A.e,{onResizeStop:(e,t,a,r)=>F(q.dR.controls_width,r),defaultSize:{width:$(q.dR.controls_width),height:"100%"},minWidth:v[q.dR.controls_width],maxWidth:"33%",enable:{right:!0},className:"col-sm-3 explore-column controls-column"},(0,O.tZ)(ft,{exploreState:e.exploreState,actions:e.actions,form_data:e.form_data,controls:e.controls,chart:e.chart,datasource_type:e.datasource_type,isDatasourceMetaLoading:e.isDatasourceMetaLoading,onQuery:S,onStop:function(){e.chart&&e.chart.queryController&&e.chart.queryController.abort()},canStopQuery:e.can_add||e.can_overwrite,errorMessage:E,chartIsStale:D})),(0,O.tZ)("div",{className:V()("main-explore-content",u?"col-sm-9":"col-sm-7")},I())),e.isSaveModalVisible&&(0,O.tZ)(Et,{addDangerToast:e.addDangerToast,actions:e.actions,form_data:e.form_data,sliceName:e.sliceName,dashboardId:e.dashboardId}))}$a.propTypes=Oa;const Ra=(0,o.$j)((function(e){var t,a,r,o,n,s,i,l,c;const{explore:d,charts:u,common:h,impressionId:p,dataMask:m,reports:g,user:f,saveModal:v}=e,{controls:b,slice:y,datasource:S,metadata:_}=d,w=(0,ee.Hu)(b),Z=null!=(t=null!=(a=w.slice_id)?a:null==y?void 0:y.slice_id)?t:0;let x="";window.location.search&&window.location.search.includes("slice_id")&&(x=sessionStorage.getItem("chartTitle")),w.extra_form_data=(0,J.on)({...w.extra_form_data},{...null==(r=m[Z])?void 0:r.ownState});const k=u[Z];let T=Number(null==(o=d.form_data)?void 0:o.dashboardId);return Number.isNaN(T)&&(T=void 0),{isDatasourceMetaLoading:d.isDatasourceMetaLoading,datasource:S,datasource_type:S.type,datasourceId:S.datasource_id,dashboardId:T,controls:d.controls,can_add:!!d.can_add,can_download:!!d.can_download,can_overwrite:!!d.can_overwrite,column_formats:null!=(n=null==S?void 0:S.column_formats)?n:null,containerId:y?`slice-container-${y.slice_id}`:"slice-container",isStarred:d.isStarred,slice:y,sliceName:null!=(s=null!=(i=null!=(l=d.sliceName)?l:null==y?void 0:y.slice_name)?i:x)?s:null,triggerRender:d.triggerRender,form_data:w,table_name:S.table_name,vizType:w.viz_type,force:!!d.force,chart:k,timeout:h.conf.SUPERSET_WEBSERVER_TIMEOUT,ownState:null==(c=m[Z])?void 0:c.ownState,impressionId:p,user:f,exploreState:d,reports:g,metadata:_,saveAction:d.saveAction,isSaveModalVisible:v.isVisible}}),(function(e){const t={...te,...G.yn,...ae,...B,...F,...re};return{actions:(0,E.DE)(t,e)}}))((0,ne.ZP)(r.memo($a)));var Ma=a(365634);(0,i.t)("Chart Options"),(0,i.t)("Use Area Proportions"),(0,i.t)("Check if the Rose Chart should use segment area instead of segment radius for proportioning"),(0,i.t)("Stacked Style"),(0,i.t)("stack"),(0,i.t)("stream"),(0,i.t)("expand"),(0,i.t)("Chart Options"),(0,i.t)("Chart Options"),(0,i.t)("Columns"),(0,i.t)("Columns to display"),le.i9.Table;const ja={form_data:{datasource:"0__table",viz_type:"table"},dataset:{id:0,type:le.i9.Table,columns:[],metrics:[],column_format:{},verbose_map:{},main_dttm_col:"",owners:[],datasource_name:"missing_datasource",name:"missing_datasource",description:null},slice:null};var Ua=a(46306);const La=(e,t="where")=>{const a={clause:t.toUpperCase(),expressionType:"SIMPLE",operator:e.op,subject:e.col,comparator:"val"in e?e.val:void 0};return e.isExtra&&Object.assign(a,{isExtra:!0,filterOptionName:`filter_${Math.random().toString(36).substring(2,15)}_${Math.random().toString(36).substring(2,15)}`}),a},za=e=>e.reduce(((e,t)=>{var a;return a=t,e.some((e=>(0,Ua.jz)(e)&&(0,Ua.jz)(a)&&e.clause===a.clause&&e.sqlExpression===a.sqlExpression||(0,Ua.Ki)(e)&&(0,Ua.Ki)(a)&&e.operator===a.operator&&e.subject===a.subject&&(!("comparator"in e)&&!("comparator"in a)||"comparator"in e&&"comparator"in a&&ra()(e.comparator,a.comparator))))||e.push(t),e}),[]),qa=(e,t)=>{const a=e.extra_form_data||{};return"time_range"in a?t.map((e=>"TEMPORAL_RANGE"===e.operator?{...e,comparator:a.time_range,isExtra:!0}:e)):t},Pa=(e,t)=>{const a=((e,t)=>{const a={__time_range:"time_range",__time_col:"granularity_sqla",__time_grain:"time_grain_sqla",__granularity:"granularity"},r={},o={};return(0,ce.Z)(t.extra_filters).forEach((e=>{if(a[e.col])e.val!==Be.vM&&(o[a[e.col]]=e.val,r[e.col]=e.val);else{const t=La({...e,isExtra:!0});o.adhoc_filters=[...(0,ce.Z)(o.adhoc_filters),t]}})),o.applied_time_extras=r,o})(0,t),r=((e,t)=>{const a={},r=t.extra_form_data||{};Object.entries(Be.gn).forEach((([e,t])=>{const o=r[e];(0,n.Z)(o)&&(a[t]=o)})),"time_grain_sqla"in r&&(a.time_grain_sqla=r.time_grain_sqla),"granularity_sqla"in r&&(a.granularity_sqla=r.granularity_sqla);const o=t.extras||{};Be.fn.forEach((e=>{const t=r[e];(0,n.Z)(t)&&(o[e]=t)})),Object.keys(o).length&&(a.extras=o),a.adhoc_filters=(0,ce.Z)(r.adhoc_filters).map((e=>({...e,isExtra:!0})));const s=(0,ce.Z)(r.filters).map((e=>La({...e,isExtra:!0})));return Object.keys(e).forEach((e=>{e.match(/adhoc_filter.*/)&&(a[e]=[...(0,ce.Z)(a[e]),...s])})),a})(e,t),o=[...Object.keys(e),...Object.keys(a),...Object.keys(r)].filter((e=>e.match(/adhoc_filter.*/))).reduce(((o,n)=>({...o,[n]:qa(t,za([...(0,ce.Z)(e[n]),...(0,ce.Z)(a[n]),...(0,ce.Z)(r[n])]))})),{});return{...e,...t,...a,...r,...o}},Fa=async e=>{try{var t;const a=await(0,s.Z)({method:"GET",endpoint:"api/v1/explore/"})(e);if((e=>{var t,a,r;return(null==e||null==(t=e.result)?void 0:t.form_data)&&(0,n.Z)(null==e||null==(a=e.result)||null==(r=a.dataset)?void 0:r.id)})(a))return a;let r=(0,i.t)("Failed to load chart data");const o=null==a||null==(t=a.result)?void 0:t.message;throw o&&(r=`${r}:\n${o}`),new Error(r)}catch(e){const t=await(0,p.O$)(e);throw new Error(t.message||t.error||(0,i.t)("Failed to load chart data."))}},Qa=()=>{const e=(0,u.eY)(h.KD.dashboardPageId),t=(a=e)&&(0,q.rV)(q.dR.dashboard__explore_context,{})[a]||null;var a;if(t){const e=(0,u.eY)(h.KD.sliceId)||0,{labelColors:a,sharedLabelColors:r,colorScheme:o,chartConfiguration:n,nativeFilters:s,filterBoxFilters:i,dataMask:l,dashboardId:c}=t,d=(0,m.Z)({chart:{id:e},filters:(0,g._f)(e,i),nativeFilters:s,chartConfiguration:n,colorScheme:o,dataMask:l,labelColors:a,sharedLabelColors:r,sliceId:e,allSliceIds:[e],extraControls:{}});return Object.assign(d,{dashboardId:c}),d}return null};function Ka(){const[e,t]=(0,r.useState)(!1),a=(0,r.useRef)(!1),n=(0,o.I0)(),{location:s}=window;return(0,r.useEffect)((()=>{const e=y(s),r=(0,u.eY)(h.KD.saveAction),o=Qa();a.current&&!r||Fa(e).then((({result:e})=>{const t=o?Pa(e.form_data,o):e.form_data;n((0,S.u)({...e,form_data:t,saveAction:r}))})).catch((e=>{n((0,S.u)(ja)),n((0,d.Gb)(e.message))})).finally((()=>{t(!0),a.current=!0})),(0,l.ZP)().source=l.Ag.explore}),[n,s]),e?(0,O.tZ)(Ra,null):(0,O.tZ)(c.Z,null)}}}]);