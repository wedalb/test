@echo off
Setlocal EnableDelayedExpansion
Set _RNDLength=2

Set _Alphanumeric=0123456789ABCDEF
Set _Str=%_Alphanumeric%987654321
:_LenLoop
IF NOT "%_Str:~18%"=="" SET _Str=%_Str:~9%& SET /A _Len+=9& GOTO :_LenLoop
SET _tmp=%_Str:~9,1%
SET /A _Len=_Len+_tmp
Set _count=0
SET _RndAlphaNum=
:_loop
Set /a _count+=1
SET _RNDCS=%Random%
Set /A _RNDCS=_RNDCS%%%_Len%

SET _RNDBS=%Random%
Set /A _RNDBS=_RNDBS%%%_Len%

SET _RNDPSN=%Random%
Set /A _RNDPSN=_RNDPSN%%%_Len%

SET _RNDSS=%Random%
Set /A _RNDSS=_RNDSS%%%_Len%

SET _RNDSU=%Random%
Set /A _RNDSU=_RNDSU%%%_Len%

SET _RndAlphaNumCS=!_RndAlphaNumCS!!_Alphanumeric:~%_RNDCS%,1!
SET _RndAlphaNumBS=!_RndAlphaNumBS!!_Alphanumeric:~%_RNDBS%,1!
SET _RndAlphaNumPSN=!_RndAlphaNumPSN!!_Alphanumeric:~%_RNDPSN%,1!
SET _RndAlphaNumSS=!_RndAlphaNumSS!!_Alphanumeric:~%_RNDSS%,1!
SET _RndAlphaNumSU=!_RndAlphaNumSU!!_Alphanumeric:~%_RNDSU%,1!

If !_count! lss %_RNDLength% goto _loop

@echo off
@echo ----------------------------------------------------------------------------------------------------------------
@echo ----------------------------------------------------------------------------------------------------------------
@echo  .----..---.  .--.  .----. .-. .-..-. . .-..-..----.
@echo { {__ {_   _}/ {} \ | {}  }| {_} || |/ \| || || {}  \
@echo .-._} } | | /  /\  \| .-. \| { } ||  .'.  || ||     /
@echo `----'  `-' `-'  `-'`-' `-'`-' `-'`-'   `-'`-'`----'
cd .\source
@echo ----------------------------------------------------------------------------------------------------------------
@echo ----------------------------------------------------------------------------------------------------------------
@echo CHANGING ALL HWIDs
@echo CS will be changed to !_RndAlphaNumCS!!_RndAlphaNumBS!!_RndAlphaNumPSN!
@echo BS will be changed to !_RndAlphaNumBS!!_RndAlphaNumPSN!!_RndAlphaNumSU!!_RndAlphaNumBS!
@echo PSN will be changed to !_RndAlphaNumPSN!!_RndAlphaNumPSN!!_RndAlphaNumPSN!!_RndAlphaNumCS!!_RndAlphaNumBS!!_RndAlphaNumPSN!!_RndAlphaNumSS!
@echo SS will be changed to !_RndAlphaNumSS!!_RndAlphaNumPSN!!_RndAlphaNumCS!!_RndAlphaNumBS!
@echo SU will be changed Automatically
cd .\source
AMIDEWINx64.EXE /CS > nul !_RndAlphaNumCS!!_RndAlphaNumBS!!_RndAlphaNumPSN!
AMIDEWINx64.EXE /BS > nul !_RndAlphaNumBS!!_RndAlphaNumPSN!!_RndAlphaNumSU!!_RndAlphaNumBS!
AMIDEWINx64.EXE /PSN > nul !_RndAlphaNumPSN!!_RndAlphaNumPSN!!_RndAlphaNumPSN!!_RndAlphaNumCS!!_RndAlphaNumBS!!_RndAlphaNumPSN!!_RndAlphaNumSS!
AMIDEWINx64.EXE /SS > nul !_RndAlphaNumSS!!_RndAlphaNumPSN!!_RndAlphaNumCS!!_RndAlphaNumBS!
AMIDEWINx64.EXE /SU > nul AUTO
@echo CS successfully changed to !_RndAlphaNumCS!!_RndAlphaNumBS!!_RndAlphaNumPSN!
@echo BS successfully changed to !_RndAlphaNumBS!!_RndAlphaNumPSN!!_RndAlphaNumSU!!_RndAlphaNumBS!
@echo PSN successfully changed to !_RndAlphaNumPSN!!_RndAlphaNumPSN!!_RndAlphaNumPSN!!_RndAlphaNumCS!!_RndAlphaNumBS!!_RndAlphaNumPSN!!_RndAlphaNumSS!
@echo SS successfully changed to !_RndAlphaNumSS!!_RndAlphaNumPSN!!_RndAlphaNumCS!!_RndAlphaNumBS!
@echo SU changed Automatically
@echo ALL HWID IDs Have Been Changed
